from typing import List

import lark
from lark import Token, Tree


class Transformer(lark.Transformer):
    def simple_import(self, children: List[Token | Tree[Token]]):
        return f"import {children[0].children[0].children[0]}"

    def from_import(self, children: List[Token | Tree[Token]]):
        module_name = list(children[0].find_data("module_name"))[0].children[0]
        import_list = list(children[1].find_data("import_list"))[0].children[0].children

        return f"from {module_name} import {','.join(import_list)}"

    def import_stmt(self, children: List[Token | Tree[Token]]):
        return children[0]

    def attribute(self, children: List[Token | Tree[Token]]):
        attr_name = children[0]
        attr_value = list(children[1].find_data("attribute_value"))[0].children[0]

        return f"{attr_name}={attr_value}"

    def interpolation(self, children: List[Token | Tree[Token]]):
        return "{" + children[0].children[0].strip() + "}"

    def text_content(self, children: List[Token | Tree[Token]]):
        return children[0]

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
        for content in element_content[0].children[0].children:
            if isinstance(content, Token):
                output.append(content)
            elif isinstance(content, str):
                output.append(content)

        output.append(f"</{tag_name}>")

        return output

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
        params_name = ""
        if len(params) > 0:
            params_name = params[0].children[0].value

        component_return = []

        component_body = list(filter(lambda v: v.data == "component_body", children))
        if len(component_body) > 0:
            component_body: Token | Tree[Token] = component_body[0]

        template_block = list(component_body.find_data("template_element"))
        for element in template_block:
            targets = element.children[0]
            if isinstance(targets, list):
                component_return.extend(targets)

        output += f"""
def {component_name}({params_name}):
    return f"{"".join(component_return)}"
"""

        return output
