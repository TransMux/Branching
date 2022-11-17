import system_module


def load():
    get_data = system_module.get_data
    textify = system_module.textify

    @get_data.after(order=textify.order + 1)
    def strip(_result: str):
        return _result[:5]

    return strip


if __name__ == '__main__':
    strip = load()
    print(strip("123456"))
