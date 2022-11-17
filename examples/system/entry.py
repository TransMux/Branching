from system_module import get_data
import plugin

if __name__ == '__main__':
    plugin.load()
    print(get_data("https://www.baidu.com"))
