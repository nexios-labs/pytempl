import ruff_api
from lark import Lark, Token, Tree

from templ.grammar import grammar
from templ.transformer import Transformer


class Engine:
    def __init__(self):
        pass

    def render(self, template_path: str, save: bool = True, format: bool = True) -> str:
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

        output = "\n".join(output).strip()
        if format:
            output = ruff_api.format_string("", output)

        if save:
            file_name = template_path.replace(template_path.split(".")[-1], "py")
            self.save(file_name, output)

            return
        return output

    def save(self, file_name: str, content: str):
        with open(file_name, "w") as f:
            f.write(content)
