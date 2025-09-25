from dataclasses import dataclass
from string import Template
from typing import List, Literal, Union

csr_template = Template(
    """
def $name():
    return "\\n".join([
    '<div id="$id">',
    '<link rel="stylesheet" href="https://pyscript.net/releases/2025.8.1/core.css">',
    '<script type="module" src="https://pyscript.net/releases/2025.8.1/core.js"></script>',
    '''<script type="$interpreter" config='{"packages": $packages}'>''',
    'import pyscript as js',
    '''$python_code''',
    'js.window.$name = $name',
    'js.document.getElementById("$id").outerHTML = $name()',
    '</script>',
    '</div>',
])
"""
)


@dataclass
class CSRComponent:
    id: str
    name: str
    content: str
    packages: List[str]
    interpreter: Union[Literal["mpy"] | Literal["py"]] = "mpy"

    def render(self):
        return csr_template.substitute(
            id=self.id,
            name=self.name,
            python_code=self.content,
            interpreter=self.interpreter,
            packages=self.packages,
        )
