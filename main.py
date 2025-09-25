from templ.engine import Engine


def main():
    engine = Engine()
    engine.render("./examples/directives.pytempl")


if __name__ == "__main__":
    main()
