import unittest

from Branching import Plugin


class TestEmpty(unittest.TestCase):
    def test_function(self):
        @Plugin
        def foo(number: int):
            return number

        self.assertEqual(foo(1), 1)

        @foo.before
        def before():
            return {"not_existed": 1}

        @foo.after
        def after(_result, not_existed: int):
            self.assertEqual(not_existed, 1)


if __name__ == '__main__':
    unittest.main()
