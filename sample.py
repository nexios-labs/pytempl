import math
from math import sqrt


def Label(props, slot):
    return (
        ""
        + '<span class="text-red bg-black" id="20" >'
        + str(sqrt(props.get("count", 1)))
        + "</span>"
        + ""
        + "<span >"
        + "Click Me"
        + "</span>"
        + ""
        + "<label >"
        + slot()
        + "</label>"
    )


def Button(props):
    return (
        ""
        + "<button onclick="
        + props.get("onclick", "")
        + " >"
        + ""
        + Label({"count": 10}, lambda: "Fancy Button")
        + "</button>"
        + ""
        + "<button >"
        + ""
        + Label(
            {"x": 0, "y": math.sqrt(4)},
            lambda: Label({"z": 8}, lambda: "Nested Fancy Button"),
        )
        + ""
        + '<img src="logo.png" alt="Logo"/>'
        + ""
        + "<br/>"
        + ""
        + "<div >"
        + "</div>"
        + ""
        + '<input type="text"/>'
        + "</button>"
    )


def Counter():
    count = 2

    def increase():
        count += 1

    def decrease():
        count -= 1

    return (
        ""
        + "<div >"
        + ""
        + "<span >"
        + "count is 0"
        + "</span>"
        + (
            ""
            + "<span >"
            + "count is 0"
            + "</span>"
            + ""
            + Label({}, lambda: "From")
            + "Hello"
            + Label({}, lambda: "To")
            + "Hello"
            if count == 0
            else (
                ""
                + "<span >"
                + "count is an even number"
                + "</span>"
                + "World"
                + Label({}, lambda: "World")
                if count == 2
                else ("")
            )
        )
        + ""
        + Button({"onclick": "do_something()"})
        + ""
        + Button({})
        + "</div>"
        + '<script type="text/javascript">'
        + "function do_something() {"
        + 'alert("doing js stuff")'
        + "}"
        + "</script>"
    )
