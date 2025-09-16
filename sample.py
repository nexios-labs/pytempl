import math
import django
from math import sqrt
from django import contrib

def Label(props, slot):

    return f"""<span class="text-red bg-black" id="20">{props.count}</span><span>Click Me</span><label>{slot()}</label>"""


def Button():

    return f"""<button>{Label({"count": 10}, lambda: f"Fancy Button")}
      {Label({"x": 0, "y": {math.sqrt(4)}}, lambda: f"{Label({"z": 8}, lambda: f"Nested Fancy Button")}")}</button>"""
