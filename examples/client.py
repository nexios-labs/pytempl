from templ import Engine


def Message():
    return Engine().client_render(
        **{
            "component": "Message",
            "python_code": """    
    import js
    from reaktiv import Signal, Effect

    js.alert("hello on the client")
    print("hello from print")
    div = js.document.createElement("div")
    div.innerHTML = "<h1>This element was created from Python</h1>"
    js.document.body.prepend(div)

    count = Signal(0)

    def count_effect():
      js.document.getElementById("count").innerHTML = count()
      print(js.document.getElementById("test"))

    # just to init
    count_effect()
    Effect(count_effect)

    def decrease():
      if count() > 0:
        count.set(count() - 1)

    def increase():
      count.set(count() + 1)

    def python_greet():
      js.document.getElementById("output").innerHTML = "Direct Python greeting! ✨"
    
    js.window.python_greet = python_greet
    js.window.increase = increase
    js.window.decrease = decrease
  """,
            "markup": ""
            + '<button onclick="python_greet()" >'
            + "Greet"
            + "</button>"
            + ""
            + '<p id="output" >'
            + "Before Python"
            + "</p>"
            + ""
            + "<div >"
            + ""
            + '<button onclick="increase()" >'
            + "Increase"
            + "</button>"
            + ""
            + '<p id="count" >'
            + count()
            + "</p>"
            + ""
            + '<button onclick="decrease()" >'
            + "Decrease"
            + "</button>"
            + "</div>"
            + '<script src="https://cdn.jsdelivr.net/pyodide/v0.28.2/full/pyodide.js">'
            + "function() {}"
            + "</script>",
        }
    )


def App():
    return (
        "" + "<h2 >" + "CSR Demo" + "</h2>" + "" + "<div >" + "" + Message() + "</div>"
    )
