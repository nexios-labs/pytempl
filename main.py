from templ.engine import Engine


def main():
    engine = Engine()
    print("Rendered template:\n", engine.render("./sample.pytempl"))


if __name__ == "__main__":
    main()
