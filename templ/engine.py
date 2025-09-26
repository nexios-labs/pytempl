import importlib
import os
from typing import List

import python_minifier
import ruff_api
from lark import Lark

from templ.grammar import grammar
from templ.transformer import Transformer


class Engine:
    def __init__(self, csr_packages: List[str] = []):
        self.csr_packages = csr_packages

    def render(
        self, template_path: str, save: bool = True, format: bool = True, minify=True
    ) -> str:
        with open(template_path, "r") as template_file:
            content = template_file.read()

        l = Lark(grammar, start="program", propagate_positions=True)
        tree = l.parse(content)

        output: str = Transformer(csr_packages=self.csr_packages).transform(tree)
        if format:
            output = ruff_api.format_string("", output.strip())

        if minify:
            output = python_minifier.minify(output)

        if save:
            file_name = template_path.replace(template_path.split(".")[-1], "py")
            self.save(file_name, output)

            return
        return output

    def save(self, file_name: str, content: str):
        with open(file_name, "w") as f:
            f.write(content)

    def _scan_directory(self, template_dir: str):
        for entry in os.listdir(template_dir):
            full_path = os.path.join(template_dir, entry)
            if os.path.isdir(full_path):
                yield from self._scan_directory(full_path)
            else:
                if full_path.endswith(".pytempl"):
                    yield full_path

    def ssr(self, template_dir: str):
        templates = list(self._scan_directory(template_dir))
        for template in templates:
            self.render(template, True, True)

    def ssg(self, template_dir: str):
        templates = list(self._scan_directory(template_dir))
        for template in templates:
            self.render(template, True, True)
            template_module = importlib.import_module(
                template.replace(".pytempl", "").replace("./", "").replace("/", ".")
            )
            if hasattr(template_module, "Page"):
                self.save(template.replace(".pytempl", ".html"), template_module.Page())
