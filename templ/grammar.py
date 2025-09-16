grammar = """
%import common.CNAME
%import common.WS
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
script_attr: CNAME "=" STRING
script_content: /.+?(?=<\/script>)/s

// Template blocks  
template_block: "<template>" template_content "</template>"
template_content: template_element*

template_element: html_element | component_call | slot_call | interpolation | text_content

// HTML elements
html_element: "<" tag_name attributes? ">" element_content "</" tag_name ">" | "<" tag_name attributes? "/>"
tag_name: CNAME
attributes: attribute+
attribute: CNAME ("=" attribute_value)?
attribute_value: STRING | CNAME
element_content: template_element*

// Component calls and slots
component_call: "@" CNAME "(" component_args? ")" component_body_call?
component_args: component_arg ("," component_arg)*
component_arg: CNAME
component_body_call: "{" template_content "}"

slot_call: "@slot()"

// Interpolation expressions
interpolation: "{{" python_expr "}}"
python_expr: /[^}]+/

// Text content (simplified - captures non-tag text)
text_content: /[^<@]+/

%import common.ESCAPED_STRING -> STRING
"""
