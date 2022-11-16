import unittest

from Branching import Plugin


class TestHookOrder(unittest.TestCase):
    def test_order(self):
        @Plugin
        def Foo(number: int):
            return number

        @Foo.before(order=1)  # first
        def before1(number: int):
            return {"number": number + 1}

        @Foo.before(order=2)  # second
        def before2(number: int):
            return {"number": number * 2}

        self.assertEqual(Foo(1), 4)

    def test_order_reverse(self):
        @Plugin
        def Foo(number: int):
            return number

        @Foo.before(order=1)  # first
        def before1(number: int):
            return {"number": number + 1}

        @Foo.before(order=-2)  # second
        def before2(number: int):
            return {"number": number * 2}

        self.assertEqual(Foo(1), 3)


if __name__ == '__main__':
    unittest.main()
