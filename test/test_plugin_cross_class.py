import unittest
from Branching import Plugin


class Foo:
    @Plugin
    def bar(self, number):
        return number


class TestPluginCrossClass(unittest.TestCase):
    def setUp(self) -> None:
        self.foo = Foo()

    def test_before(self):
        @Foo.bar.before  # 动态挂载，全部生效
        def before(number: int):
            return {"number": number + 1}

        self.assertEqual(self.foo.bar(1), 2)
        self.assertEqual(before(1), {"number": 2})
        before.remove()
        self.assertEqual(self.foo.bar(1), 1)
        before.mount()
        self.assertEqual(self.foo.bar(1), 2)
        before.remove()

    def test_after(self):
        @Foo.bar.after
        def after(_result):
            return _result + 1

        self.assertEqual(self.foo.bar(1), 2)
        after.remove()

    def test_both(self):
        @Foo.bar.before
        def before(number: int):
            return {"number": number + 1}

        @Foo.bar.after
        def after(_result):
            return _result + 1

        self.assertEqual(self.foo.bar(1), 3)
        before.remove()
        after.remove()
