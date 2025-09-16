from lark import Lark, Token, Tree

from templ.grammar import grammar
from templ.transformer import Transformer


class Engine:
    def __init__(self):
        pass

    def render(self, template_path: str) -> str:
        with open(template_path, "r") as template_file:
            content = template_file.read()

        l = Lark(grammar, start="program")
        tree = l.parse(content)

        output = []
        transformed: Tree[Token] = Transformer().transform(tree)
        for i in transformed.children:
            if i is None:
                continue
            output.append(i)

        return "\n".join(output)
