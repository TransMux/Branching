import unittest
from Branching import On
from system_module import get_data
import plugin


class TestEmpty(unittest.TestCase):
    def test_function(self):
        plugin.load()
        On()
        self.assertEqual(get_data("https://www.baidu.com"), "<!DOC")
