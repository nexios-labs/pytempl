import math
from math import sqrt


def Label(props, slot):
    return (
        ""
        + '<span class="text-red bg-black" id="20" >'
        + str(sqrt(int(props.get("count", "1"))))
        + "</span>"
        + ""
        + "<span >"
        + props.get("text", "Click Me")
        + "</span>"
        + ""
        + "<label >"
        + slot()
        + "</label>"
    )


def Button(props, slot):
    return (
        ""
        + "<button onclick="
        + props.get("onclick", "")
        + ' class="demo-button" >'
        + ""
        + Label(
            {"count": props.get("count", 4), "text": props.get("label", "Button")},
            lambda: slot(),
        )
        + "</button>"
    )


def TodoItem(props):
    return (
        ""
        + '<li class="todo-item" >'
        + (
            "" + '<input type="checkbox" checked="true"/>'
            if props.get("done", False)
            else ("" + '<input type="checkbox"/>')
        )
        + (
            ""
            + '<span class="completed" >'
            + ""
            + props.get("text", "Todo item")
            + "</span>"
            if props.get("done", False)
            else ("" + "<span >" + "" + props.get("text", "Todo item") + "</span>")
        )
        + ""
        + Label({"count": props.get("priority", 1)}, lambda: "Priority")
        + "</li>"
    )


def Demo():
    colors = ["red", "green", "blue", "purple", "orange"]
    count = 3
    todos = [
        {"text": "Learn template engine", "done": True, "priority": 9},
        {"text": "Build awesome app", "done": False, "priority": 16},
        {"text": "Deploy to production", "done": False, "priority": 25},
    ]

    def get_status():
        return "active" if count > 0 else "inactive"

    def get_message():
        return f"System has {count} items"

    return (
        ""
        + '<div class="demo-container" >'
        + ""
        + "<h1 >"
        + "Template Engine Demo"
        + "</h1>"
        + ""
        + '<div class="section" >'
        + ""
        + "<h2 >"
        + "Basic Components & Math"
        + "</h2>"
        + ""
        + "<p >"
        + "Current count:"
        + "<strong >"
        + str(count)
        + "</strong>"
        + "sqrt:"
        + str(math.sqrt(count) if count > 0 else 0)
        + "</p>"
        + ""
        + Button(
            {
                "onclick": "toggleCount()",
                "label": "Toggle",
                "count": str(count * count),
            },
            lambda: "Toggle Count",
        )
        + ""
        + Button(
            {"onclick": "showAlert('Hello World!')", "label": "Alert", "count": 64},
            lambda: "Show Alert",
        )
        + "</div>"
        + ""
        + '<div class="section" >'
        + ""
        + "<h2 >"
        + "Conditional Rendering"
        + "</h2>"
        + ""
        + "<div class="
        + "status-"
        + get_status()
        + " >"
        + (
            ""
            + '<p class="warning" >'
            + "⚠️ No items available"
            + "</p>"
            + ""
            + Label({"count": 1, "text": "Empty State"}, lambda: "System Idle")
            if count == 0
            else (
                ""
                + '<p class="info" >'
                + "✅ Low activity mode"
                + "</p>"
                + ""
                + Label(
                    {"count": count * count, "text": "Low Mode"}, lambda: get_message()
                )
                if count <= 3
                else (
                    ""
                    + '<p class="success" >'
                    + "🚀 High activity mode"
                    + "</p>"
                    + ""
                    + Label(
                        {"count": count * 4, "text": "High Mode"},
                        lambda: "System is busy!",
                    )
                )
            )
        )
        + "</div>"
        + "</div>"
        + ""
        + '<div class="section" >'
        + ""
        + "<h2 >"
        + "Loops & Collections"
        + "</h2>"
        + ""
        + '<div class="color-palette" >'
        + ""
        + "<h3 >"
        + "Available Colors:"
        + "</h3>"
        + "".join(
            [
                ""
                + "<div class="
                + "color-item color-"
                + color
                + " >"
                + ""
                + Label(
                    {"count": len(color), "text": color.title()},
                    lambda: "Color: " + color,
                )
                + ""
                + '<span class="color-code" >'
                + "#"
                + color
                + "</span>"
                + "</div>"
                for color in colors
            ]
        )
        + "</div>"
        + ""
        + '<div class="todo-list" >'
        + ""
        + "<h3 >"
        + "Todo List:"
        + "</h3>"
        + ""
        + "<ul >"
        + "".join(
            [
                ""
                + TodoItem(
                    {
                        "text": todo["text"],
                        "done": todo["done"],
                        "priority": todo["priority"],
                    }
                )
                for todo in todos
            ]
        )
        + "</ul>"
        + "</div>"
        + "</div>"
        + ""
        + '<div class="section" >'
        + ""
        + "<h2 >"
        + "Nested Components"
        + "</h2>"
        + ""
        + '<div class="nested-demo" >'
        + ""
        + Button(
            {"onclick": "showAlert('Outer button')", "count": 100},
            lambda: "Outer Button with"
            + Label({"count": 49, "text": "Inner"}, lambda: "Nested Label")
            + "and more content",
        )
        + ""
        + '<div class="button-group" >'
        + "".join(
            [
                ""
                + Button(
                    {"onclick": "showAlert('hello')", "count": (i + 1) * (i + 1)},
                    lambda: "Dynamic Button" + str(i + 1),
                )
                for i in range(3)
            ]
        )
        + "</div>"
        + "</div>"
        + "</div>"
        + ""
        + '<div class="section" >'
        + ""
        + "<h2 >"
        + "Mixed Content"
        + "</h2>"
        + ""
        + '<div class="mixed-content" >'
        + ""
        + "<p >"
        + "This section combines:"
        + "</p>"
        + ""
        + "<ul >"
        + ""
        + "<li >"
        + "Static HTML content"
        + "</li>"
        + ""
        + "<li >"
        + "Dynamic Python expressions: Count squared ="
        + str(count * count)
        + "</li>"
        + ""
        + "<li >"
        + "Component composition with"
        + "@Label and @Button"
        + "</li>"
        + ""
        + "<li >"
        + "JavaScript interactions"
        + "</li>"
        + "</ul>"
        + ""
        + Label(
            {"count": str(sum(range(count + 1))), "text": "Sum"},
            lambda: "Mathematical computation: Sum of 0 to"
            + str(count)
            + "="
            + str(sum(range(count + 1))),
        )
        + ""
        + "<br/>"
        + ""
        + Button(
            {"onclick": "showAlert('Demo completed!')", "count": 144},
            lambda: "Finish Demo",
        )
        + "</div>"
        + "</div>"
        + "</div>"
        + '<script type="text/javascript">'
        + "function showAlert(message) {"
        + 'alert("Demo Alert: " + message);'
        + "}"
        + ""
        + "function toggleCount() {"
        + "count = count === 0 ? 5 : 0;"
        + 'console.log("Count toggled to:", count);'
        + "}"
        + "</script>"
    )


def App():
    return (
        ""
        + "<html >"
        + ""
        + "<head >"
        + ""
        + "<title >"
        + "Template Engine Demo"
        + "</title>"
        + "</head>"
        + ""
        + "<body >"
        + ""
        + Demo()
        + "</body>"
        + "</html>"
    )
