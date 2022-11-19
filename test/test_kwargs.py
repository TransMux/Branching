import unittest
from Branching import Plugin


class TestKwargs(unittest.TestCase):
    def test_kwargs(self):
        @Plugin
        def target(**kwargs):
            return kwargs

        @target.before
        def before(number):
            return {"number": number + 1}

        @target.after
        def after(_result):
            return _result["number"] + 1

        self.assertEqual(target(number=1), 3)
