from templ.engine import Engine


def main():
    engine = Engine()
    engine.render("./examples/demo.pytempl", format=True)
    engine.render("./examples/sample.pytempl", format=True)
    engine.ssg("./examples/blog")


if __name__ == "__main__":
    main()
