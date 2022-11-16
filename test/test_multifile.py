import unittest

from target import hooked


class TestMultiFile(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(hooked(1), 2)

        @hooked.before
        def hooked_before(number: int):
            return {"number": number + 1}

        self.assertEqual(hooked(1), 3)

        hooked_before.remove()

        self.assertEqual(hooked(1), 2)


if __name__ == '__main__':
    unittest.main()
