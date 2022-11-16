import unittest

from target import foo, Foo


class TestImport(unittest.TestCase):
    def test_function(self):
        self.assertEqual(foo(1), 1)

        @foo.before
        def before(number: int):
            return {"number": number + 1}

        self.assertEqual(foo(1), 2)

        before.remove()
        self.assertEqual(foo(1), 1)

        before.mount()
        self.assertEqual(foo(1), 2)

        before.remove()

    def test_method(self):
        foo_ = Foo()
        self.assertEqual(foo_.foo(1), 1)

        @foo_.foo.before
        def before(number: int):
            return {"number": number + 1}

        self.assertEqual(foo_.foo(1), 2)

        before.remove()
        self.assertEqual(foo_.foo(1), 1)

        before.mount()
        self.assertEqual(foo_.foo(1), 2)

        before.remove()


if __name__ == '__main__':
    unittest.main()
