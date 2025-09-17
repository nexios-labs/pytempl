import math
from math import sqrt


def Label(props, slot):

    return (
        '<span class="text-red bg-black" id="20">'
        + str(sqrt(props.get("count", 1)))
        + "</span>"
        + ""
        + "<span>"
        + "Click Me"
        + "</span>"
        + ""
        + "<label>"
        + slot()
        + "</label>"
    )


def Button(props):

    return (
        '<button onclick="do_something()">'
        + Label({"count": 10}, lambda: "Fancy Button")
        + "</button>"
        + ""
        + "<button>"
        + Label(
            {"x": 0, "y": math.sqrt(4)},
            lambda: Label({"z": 8}, lambda: "Nested Fancy Button"),
        )
        + "</button>"
    )


def Counter():

    return (
        "<div>"
        + "if count == 0:"
        + "<span>"
        + "count is 0"
        + "</span>"
        + "elif count % 2:"
        + "<span>"
        + "count is an even number"
        + "</span>"
        + "else:"
        + "<span>"
        + "count is an odd number"
        + "</span>"
        + ""
        + Button({"onclick": "do_something"}, lambda: "Decrease")
        + ""
        + Button({}, lambda: "Increase")
        + "</div>"
        + '<script type="text/javascript">'
        + "function do_something() {"
        + 'alert("doing js stuff")'
        + "}"
        + "</script>"
    )
