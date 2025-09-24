from dataclasses import dataclass
from string import Template
from typing import List

import lark
from lark import Token, Tree

function_template = Template(
    """
def $name($params):
    $python_code
    return ( $markup )
"""
)

pyodide_template = Template(
    """
let pyodide;

async function main(){
    pyodide = await loadPyodide();
    await pyodide.loadPackage("https://files.pythonhosted.org/packages/dd/3a/0e8db597f12cd77e61ebe915a3f9a6f83cff0501a3980dec5be049858a8a/reaktiv-0.19.2-py3-none-any.whl");

    pyodide.runPython(`
    $python_code
    `);
    }
main();
"""
)


@dataclass
class Script:
    type: str
    content: str


@dataclass
class Attribute:
    name: str
    value: str


class Transformer(lark.Transformer):
    def simple_import(self, children: List[Token | Tree[Token]]):
        return f"import {children[0].children[0].children[0]}"

    def from_import(self, children: List[Token | Tree[Token]]):
        module_name = ".".join(list(children[0].find_data("module_name"))[0].children)
        import_list = list(children[1].find_data("import_list"))[0].children[0].children

        return f"from {module_name} import {','.join(import_list)}"

    def import_stmt(self, children: List[Token | Tree[Token]]):
        return children[0]

    def interpolation(self, children: List[Token | Tree[Token]]):
        # For INTERPOLATION_BLOCK terminal: {{ expression }}
        content = children[0].value  # Get the full {{ ... }} content
        # Remove the {{ and }} and extract the Python expression
        python_expr = content[2:-2].strip()

        return python_expr

    def quoted_interpolation(self, children: List[Token | Tree[Token]]):
        # For QUOTED_INTERPOLATION terminal: "{{ expression }}"
        content = children[0].value  # Get the full "{{ ... }}" content
        # Remove the quotes and {{ }} and extract the Python expression
        python_expr = content[3:-3].strip()  # Remove "{{ and }}"

        return "' +" + python_expr + "+'"

    def if_clause(self, children: List[Token | Tree[Token]]):
        condition = children[0].value.strip()  # PYTHON_CONDITION terminal

        block_content = "+".join(
            list(map(lambda v: "+".join(v.children), children[1:]))
        )
        return {"type": "if", "condition": condition, "content": block_content}

    def elif_clause(self, children: List[Token | Tree[Token]]):
        condition = children[0].value.strip()  # PYTHON_CONDITION terminal
        # block_content = "+".join(children[1:][0].children)
        block_content = "+".join(
            list(map(lambda v: "+".join(v.children), children[1:]))
        )
        return {"type": "elif", "condition": condition, "content": block_content}

    def else_clause(self, children: List[Token | Tree[Token]]):
        # else clause has no condition, all children are template elements
        block_content = "+".join(list(map(lambda v: "+".join(v.children), children)))
        return {"type": "else", "content": block_content}

    def if_statement(self, children: List[Token | Tree[Token]]):
        # children contains: [if_clause, elif_clause*, else_clause?]
        clauses = children

        # Build the nested conditional expression from right to left
        result = "''"  # Default empty string if no conditions match

        # Process clauses in reverse order to build proper nesting
        for clause in reversed(clauses):
            if clause["type"] == "else":
                result = f"({clause['content']})"
            elif clause["type"] in ["if", "elif"]:
                result = f"({clause['content']} if {clause['condition']} else {result})"

        return result

    def for_loop(self, children: List[Token | Tree[Token]]):
        item = children[0]
        items = children[1]
        body = "+".join(["+".join(child.children) for child in children[2:]])
        result = f"''.join([{body} for {item} in {items}])"

        return result

    def control_flow(self, children: List[Token | Tree[Token]]):
        return "".join(children)

    def body_text(self, children: List[Token | Tree[Token]]):
        return self.text_content(children)

    def text_content(self, children: List[Token | Tree[Token]]):
        text = children[0].value.strip()
        return f"'{text}'"

    def attribute(self, children: List[Token | Tree[Token]]):
        attr_name = children[0]
        attr_value = list(children[1].find_data("attribute_value"))[0].children[0]

        return f"{attr_name}={attr_value}"

    def doctype(self, children: List[Token | Tree[Token]]):
        return f"'<!DOCTYPE " + children[0].value + ">'"

    def html_element(self, children: List[Token | Tree[Token]]):
        output = []
        tag_name = children[0].children[0]

        # Collect attributes if present
        attributes_nodes = list(filter(lambda v: v.data == "attributes", children))
        has_attributes = len(attributes_nodes) > 0
        attrs_str = ""
        if has_attributes:
            attributes: Token | Tree[Token] = attributes_nodes[0]
            attrs_str = " " + " ".join(attributes.children)

        element_content_nodes = list(
            filter(lambda v: v.data == "element_content", children)
        )
        is_self_closing = len(element_content_nodes) == 0

        if is_self_closing:
            return f"'<{tag_name}{attrs_str}/>'"

        opening_tag = []
        opening_tag.append(f"'<{tag_name}")
        if has_attributes:
            opening_tag.append(attrs_str)
        opening_tag.append(" >'")
        output.append("".join(opening_tag).strip())

        for content in element_content_nodes[0].children:
            if isinstance(content, str):
                output.append(content)

        output.append(f"'</{tag_name}>'")

        return "+".join(output)

    def script_attr(self, children: List[Token | Tree[Token]]):
        attr_name = children[0].value
        attr_value = children[1].children[0].value

        return Attribute(attr_name, attr_value)

    def script_attrs(self, children: List[Token | Tree[Token]]):
        return children

    def script_block(self, children: List[Token | Tree[Token]]):
        def get_attr(attrs: List[Attribute], name: str):
            attr = list(filter(lambda v: v.name == name, attrs))
            if not attr:
                return ""
            value = attr[0].value.strip('"')

            return value

        script = []
        attrs: List[Attribute] = children[0]
        script_type = get_attr(attrs, "type")
        mode = get_attr(attrs, "mode")
        if script_type == "text/python":
            if mode == "client":
                attrs = list(filter(lambda v: v.name != "mode", attrs))
                attrs = list(
                    map(
                        lambda v: (
                            Attribute(v.name, '"text/javascript"')
                            if v.name == "type"
                            else v
                        ),
                        attrs,
                    )
                )

                script.append(
                    "'<script "
                    + " ".join([f"{attr.name}={attr.value}" for attr in attrs])
                    + ">'"
                )

                content = (
                    list(children[1].find_data("script_content"))[0]
                    .children[0]
                    .value.split("\n")
                )
                script.append(
                    "'''"
                    + pyodide_template.substitute(
                        python_code="\n".join(content),
                    )
                    + "'''"
                )

                script.append("'</script>'")

                return Script("javascript", "".join(script))
            for inner in list(children[1].find_data("script_content"))[0].children:
                script.append(inner)

            return Script("python", "\n".join(script))
        else:
            script.append(
                "'<script "
                + " ".join([f"{attr.name}={attr.value}" for attr in attrs])
                + ">'"
            )

            if len(children) > 1:
                for inner in (
                    list(children[1].find_data("script_content"))[0]
                    .children[0]
                    .value.strip()
                    .split("\n")
                ):
                    script.append(
                        "'" + inner.strip() + "'",
                    )
            script.append("'</script>'")

            return Script("javascript", "+".join(script))

    def style_block(self, children: List[Token | Tree[Token]]):
        return '"""<style>' + children[0].children[0] + '</style>"""'

    def dict_literal(self, children: List[Token | Tree[Token]]):
        if len(children) == 0:
            return "{}"

        items = children[0].children

        return "{" + ", ".join(items) + "}"

    def dict_item(self, children: List[Token | Tree[Token]]):
        key = children[0]
        value = children[1]

        return f"{key}: {value}"

    def list_literal(self, children: List[Token | Tree[Token]]):
        items = children[0].children

        return "[" + "".join(items) + "]"

    def template_element(self, children: List[Token | Tree[Token]]):
        return "+".join(children)

    def template_block(self, children: List[Token | Tree[Token]]):
        result = []
        for child in children:
            result.extend(child.children)

        return "+".join(result)

    def component_body_call(self, children: List[Token | Tree[Token]]):
        body_content = []
        if len(children) > 0:
            body_elements = children[0].children  # body_content children
            for element in body_elements:
                element: str = element.children[0]
                if len(element.strip("'")) == 0:
                    continue
                body_content.append(element)

        return "+".join(body_content)

    def component_call(self, children: List[Token | Tree[Token]]):
        component_name = children[0].children[0]
        component_args = []

        # Handle regular arguments
        if len(children) > 1 and hasattr(children[1], "children"):
            for arg in children[1].children:
                if hasattr(arg, "children") and arg.children:
                    component_args.append(str(arg.children[0]))
                else:
                    component_args.append(str(arg))

        # Handle body call (slot content) - pass as last argument
        if len(children) >= 2:  # Has component_body_call
            slot_content = children[-1]
            if isinstance(slot_content, Tree):
                slot_content = "".join(slot_content.children[0].children)
            if slot_content.startswith("''+"):
                slot_content = slot_content[3:]
            if slot_content.startswith("''"):
                slot_content = slot_content[2:]

            component_args.append(f"lambda: {slot_content}")  # Pass as string to slot

        args_str = ", ".join(component_args)
        call = f"{component_name}({args_str})"

        return call

    def component_def(self, children: List[Token | Tree[Token]]):
        output = ""

        component_name = (
            list(
                list(children[0].find_data("component_name"))[0].find_pred(
                    lambda v: isinstance(v, Tree)
                )
            )[0]
            .children[0]
            .value
        )
        params = list(filter(lambda v: v.data == "params", children))
        params_name = []
        if len(params) > 0:
            params_name.append(params[0].children[0].value)

        markup = []
        python = []
        javascript = []

        component_body = list(filter(lambda v: v.data == "component_body", children))
        if len(component_body) > 0:
            component_body: Token | Tree[Token] = component_body[0]

        for blocks in list(component_body.find_data("component_element")):
            for block in blocks.children:
                if isinstance(block, Script):
                    if block.type == "javascript":
                        javascript.append(block.content)
                    elif block.type == "python":
                        python.append(block.content)
                elif isinstance(block, str):
                    markup.append(block)

        has_slot = component_body.pretty("").find("slot") >= 0
        if has_slot:
            params_name.append("slot")

        template_block = list(component_body.find_data("template_element"))
        for element in template_block:
            targets = element.children[0]
            if isinstance(targets, list):
                markup.extend(targets)
            elif isinstance(targets, str):
                markup.append(targets)

        output += function_template.substitute(
            name=component_name,
            params=", ".join(params_name),
            python_code="\n".join(f"    {line}" for line in python),
            markup="+".join([*markup, *javascript]),
        )

        return output
