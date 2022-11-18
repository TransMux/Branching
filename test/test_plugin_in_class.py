import unittest
from Branching import Plugin

"""
显式加载
import plugin...
依赖传递
import pluginA, -> PluginB
去除插件显式调用
call_before()...
插件优先级
level
去除插件
plugin.remove()

target(num, a=2)

target(1,2) *args = [1,2]

"""


class TestPluginInClass(unittest.TestCase):
    def test_before(self):
        @Plugin
        def target(number: int):
            return number

        @target.before
        def before(number: int):
            return {"number": number + 1}

        self.assertEqual(target(1), 2)

    def test_after(self):
        @Plugin
        def target(number: int):
            return number

        @target.after
        def after(_result):
            return _result + 1

        self.assertEqual(target(1), 2)

    def test_both(self):
        @Plugin
        def target(number: int):
            return number

        @target.before
        def before(number: int):
            return {"number": number + 1}

        @target.after
        def after(_result):
            return _result + 1

        self.assertEqual(target(1), 3)
