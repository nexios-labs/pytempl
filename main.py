from templ.engine import Engine


def main():
    engine = Engine()
    print(engine.render("./sample.pytempl"))


if __name__ == "__main__":
    main()
