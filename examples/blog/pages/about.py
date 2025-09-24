from examples.blog.layout import Layout


def Page():
    return "" + Layout(lambda: "<p >" + "this is the about page" + "</p>")
