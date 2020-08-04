import unittest
from lib.core.pretty_printer import PrettyPrint


class MyTest(unittest.TestCase):
    def test(self):
        lines = ['test line 1', 'test line 2']
        printer = PrettyPrint(lines=lines)
        self.assertEqual(len(lines), 2)
        self.assertEqual(printer.total, 2)
