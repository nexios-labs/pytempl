from string import Template
from typing import List

import lark
from lark import Token, Tree

function_template = Template(
    '''
def $name($params):
$python_code
    return f"""$markup"""
'''
)


class Transformer(lark.Transformer):
    def simple_import(self, children: List[Token | Tree[Token]]):
        return f"import {children[0].children[0].children[0]}"

    def from_import(self, children: List[Token | Tree[Token]]):
        module_name = list(children[0].find_data("module_name"))[0].children[0]
        import_list = list(children[1].find_data("import_list"))[0].children[0].children

        return f"from {module_name} import {','.join(import_list)}"

    def import_stmt(self, children: List[Token | Tree[Token]]):
        return children[0]

    def interpolation(self, children: List[Token | Tree[Token]]):
        return "{" + children[0].children[0].strip() + "}"

    def body_text(self, children: List[Token | Tree[Token]]):
        return self.text_content(children)

    def text_content(self, children: List[Token | Tree[Token]]):
        return children[0].value

    def attribute(self, children: List[Token | Tree[Token]]):
        attr_name = children[0]
        attr_value = list(children[1].find_data("attribute_value"))[0].children[0]

        return f"{attr_name}={attr_value}"

    def html_element(self, children: List[Token | Tree[Token]]):
        output = []
        tag_name = children[0].children[0]

        output.append(f"<{tag_name}")

        attributes = list(filter(lambda v: v.data == "attributes", children))
        if len(attributes) > 0:
            attributes: Token | Tree[Token] = attributes[0]

            output.append(" " + " ".join(attributes.children))

        output.append(f">")

        element_content = list(filter(lambda v: v.data == "element_content", children))
        for content in element_content[0].children:
            content = content.children[0]
            output.append(content)

        output.append(f"</{tag_name}>")

        return output

    def dict_literal(self, children: List[Token | Tree[Token]]):
        items = children[0].children

        return "{" + ", ".join(items) + "}"

    def dict_item(self, children: List[Token | Tree[Token]]):
        key = children[0]
        value = children[1]

        return f"{key}: {value}"

    def list_literal(self, children: List[Token | Tree[Token]]):
        items = children[0].children

        return "[" + "".join(items) + "]"

    def component_body_call(self, children: List[Token | Tree[Token]]):
        body_content = []
        if len(children) > 0:
            body_elements = children[0].children  # body_content children
            for element in body_elements:
                if hasattr(element, "children") and element.children:
                    body_content.append(str(element.children[0]))
                else:
                    body_content.append(str(element))

        return "".join(body_content)

    def component_call(self, children: List[Token | Tree[Token]]):
        component_name = children[0]
        component_args = []

        # Handle regular arguments
        if len(children) > 1 and hasattr(children[1], "children"):
            for arg in children[1].children:
                if hasattr(arg, "children") and arg.children:
                    component_args.append(str(arg.children[0]))
                else:
                    component_args.append(str(arg))

        # Handle body call (slot content) - pass as last argument
        if len(children) > 2:  # Has component_body_call
            slot_content = children[2]  # The body content
            component_args.append(
                f'lambda: f"{slot_content.strip()}"'
            )  # Pass as string to slot

        args_str = ", ".join(component_args)
        return "{" + f"{component_name}({args_str})" + "}"

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

        has_slot = component_body.pretty("").find("slot") >= 0
        if has_slot:
            params_name.append("slot")

        template_block = list(component_body.find_data("template_element"))
        for element in template_block:
            targets = element.children[0]
            if isinstance(targets, list):
                markup.extend(targets)

        output += function_template.substitute(
            name=component_name,
            params=", ".join(params_name),
            python_code="\n".join(f"    {line}" for line in python),
            markup="".join([*markup, *javascript]),
        )

        return output
