import math
from math import sqrt


def Label(props, slot):

    return (
        '<span class="text-red bg-black" id="20">'
        + str(sqrt(props.count))
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


def Button():

    return (
        "<button>"
        + Label({"count": 10}, lambda: "Fancy Button")
        + ""
        + Label(
            {"x": 0, "y": str(math.sqrt(4))},
            lambda: Label({"z": 8}, lambda: "Nested Fancy Button"),
        )
        + "</button>"
    )
