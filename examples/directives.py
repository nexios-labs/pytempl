_E='</div>'
_D='</script>'
_C='import pyscript as js'
_B='<script type="module" src="https://pyscript.net/releases/2025.8.1/core.js"></script>'
_A='<link rel="stylesheet" href="https://pyscript.net/releases/2025.8.1/core.css">'
def Demo():return'\n'.join(['<div id="Demo-e672e36f1c2d8cb5fe9b">',_A,_B,'<script type="mpy" config=\'{"packages": []}\'>',_C,'\ndef Demo():\n        \n    print("hello")\n  \n    return ( \'\'+\'<p>\'+\'Hello, World\'+\'</p>\' )\n','js.window.Demo = Demo','js.document.getElementById("Demo-e672e36f1c2d8cb5fe9b").outerHTML = Demo()',_D,_E])
def AnotherDemo():return'\n'.join(['<div id="AnotherDemo-7c7a1da612b9249ab56a">',_A,_B,'<script type="py" config=\'{"packages": []}\'>',_C,'\ndef AnotherDemo():\n        \n    print("hello 2")\n  \n    return ( \'\'+\'<p>\'+\'Hello, 2\'+\'</p>\' )\n','js.window.AnotherDemo = AnotherDemo','js.document.getElementById("AnotherDemo-7c7a1da612b9249ab56a").outerHTML = AnotherDemo()',_D,_E])
def App():return''+'<p>'+'Some contents are being rendered from by pyodide, slow thing, please wait'+'</p>'+''+Demo()+''+AnotherDemo()