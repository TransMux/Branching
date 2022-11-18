import unittest
from Branching import Plugin, On, Off, Toggle


class TestToggle(unittest.TestCase):

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

        Off()

        self.assertEqual(target(1), 1)

        On()

        self.assertEqual(target(1), 3)

        Toggle()

        self.assertEqual(target(1), 1)
