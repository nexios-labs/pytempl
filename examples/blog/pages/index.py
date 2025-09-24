from examples.blog.layout import Layout


def Page():
    return "" + Layout(
        lambda: "<p >"
        + "this is the home page"
        + "</p>"
        + "<p >"
        + "this is the home page"
        + "</p>"
        + "<p >"
        + "this is the home page"
        + "</p>"
    )
