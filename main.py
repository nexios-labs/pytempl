from templ.engine import Engine


def main():
    engine = Engine()
    # engine.render("./examples/demo.pytempl", format=True)
    # engine.render("./examples/sample.pytempl", format=True)

    client_raw = open("./examples/client.pytempl", "r").read()
    client_output = engine.server_render(client_raw, format=True)
    with open("./examples/client.py", "w") as f:
        f.write(client_output)


if __name__ == "__main__":
    main()
