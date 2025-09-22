import ruff_api
from lark import Lark, Token, Tree

from templ.grammar import grammar
from templ.transformer import Transformer, pyodide_template


class Engine:
    def __init__(self):
        pass

    def server_render(self, content: str, format: bool = True):
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

        return output

    def client_render(self, **args: dict):
        output = "".join(
            [
                args.get("component", ""),
                args.get("markup", ""),
                '<script type="text/javascript">',
                pyodide_template.substitute(python_code=args.get("python_code")),
                "</script >",
            ]
        )

        return output

    def save(self, file_name: str, content: str):
        with open(file_name, "w") as f:
            f.write(content)
