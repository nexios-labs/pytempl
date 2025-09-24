def Layout(slot):
    return (
        ""
        + "<!DOCTYPE  html>"
        + ""
        + "<html >"
        + ""
        + "<head >"
        + ""
        + "<title >"
        + "Blog Demo"
        + "</title>"
        + "</head>"
        + ""
        + "<body >"
        + ""
        + slot()
        + "</body>"
        + "</html>"
    )
