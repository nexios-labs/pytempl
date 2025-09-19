grammar = """
%import common.CNAME
%import common.WS
%import common.ESCAPED_STRING -> STRING
%import common.NUMBER
%import common.SH_COMMENT
%ignore WS
%ignore SH_COMMENT

program: (import_stmt | component_def)+

// Import statements
import_stmt: simple_import | from_import
simple_import: "import" module_list
from_import: "from" module_name "import" import_list
module_list: module_name ("," module_name)*
import_list: import_item ("," import_item)*
module_name: CNAME ("." CNAME)*
import_item: CNAME

// Component definitions
component_def: "component" component_name "(" params? ")" "{" component_body "}"
component_name: CNAME
params: CNAME ("," CNAME)*
component_body: component_element*

component_element: script_block | template_block

// Script blocks
script_block: "<script" script_attrs? ">" script_content "</script>"
script_attrs: script_attr+
script_attr: CNAME ("=" script_value)?
script_value: STRING | CNAME
script_content: /.+?(?=<\/script>)/s

// Template blocks
template_block: "<template>" template_content "</template>"
template_content: template_element*

template_element: control_flow | component_call | html_element | interpolation | text_content

// HTML elements
html_element: "<" tag_name attributes? ">" element_content "</" tag_name ">" | "<" tag_name attributes? "/>"
tag_name: CNAME
attributes: attribute+
attribute: CNAME ("=" attribute_value)?
attribute_value: quoted_interpolation | INTERPOLATION_BLOCK | STRING | CNAME
element_content: template_element*

// Component calls
component_call: "@" CNAME "(" component_args? ")" component_body_call?
component_args: component_arg ("," component_arg)*
component_arg: dict_literal | list_literal | interpolation | STRING | NUMBER | CNAME
component_body_call: "{" body_content "}"

// Body content for component calls
body_content: body_element*
body_element: control_flow | component_call | html_element | interpolation | body_text

// Python literals
dict_literal: "{" dict_items* "}"
dict_items: dict_item ("," dict_item)*
dict_item: (STRING | CNAME) ":" (STRING | NUMBER | CNAME | interpolation)

list_literal: "[" list_items? "]"
list_items: list_item ("," list_item)*
list_item: STRING | NUMBER | CNAME | interpolation

control_flow: if_statement | for_loop

// If statements
if_statement: if_clause elif_clause* else_clause?
if_clause: "if" PYTHON_CONDITION "{" body_element* "}"
elif_clause: "elif" PYTHON_CONDITION "{" body_element* "}"
else_clause: "else" "{" body_element* "}"

for_loop: "for" CNAME "in" (CNAME | interpolation) "{" body_element* "}"

// Interpolation expressions - using terminal for complete block
interpolation: INTERPOLATION_BLOCK
quoted_interpolation: QUOTED_INTERPOLATION

// Text content
text_content: TEXT_CONTENT
body_text: BODY_TEXT

// Terminals - with high priority
PYTHON_CONDITION.8: /(?:[^{()[\]"']|\([^)]*\)|\[[^\]]*\]|"[^"]*"|'[^']*')+(?=\s*\{)/
QUOTED_INTERPOLATION.10: /"\{\{[^}]*\}\}"/
INTERPOLATION_BLOCK.9: /\{\{[^}]*\}\}/
TEXT_CONTENT.5: /(?!if\b|elif\b|else\b)[^<@{]+/
BODY_TEXT.5: /(?!if\b|elif\b|else\b)[^<@{}]+/
"""
