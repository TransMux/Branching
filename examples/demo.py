from Branching import Plugin


class Demo:
    def __init__(self, version):
        self.version = version

    @Plugin
    def render(self):
        return f"<{self.version}>"


class Hook:

    @staticmethod
    @Demo.render.after
    def render_v2(_result, self: Demo):
        if self.version == "v2":
            return _result + "v2"
        else:
            return _result


if __name__ == "__main__":
    demo = Demo("v1")
    print(demo.render())
    demo.version = "v2"
    print(demo.render())
