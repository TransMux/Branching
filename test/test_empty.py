import unittest

from target import foo


class TestEmpty(unittest.TestCase):
    def test_function(self):
        self.assertEqual(foo(1), 1)

        @foo.before
        def before(number: int):
            return None

        self.assertEqual(foo(1), 1)

        before.remove()
        self.assertEqual(foo(1), 1)

        before.mount()
        self.assertEqual(foo(1), 1)

        before.remove()


if __name__ == '__main__':
    unittest.main()
