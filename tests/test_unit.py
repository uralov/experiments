# -*- coding: utf-8 -*-
import unittest


def sum_args(*args):
    total = lambda x, y: x + y
    return reduce(total, args)


class Test(unittest.TestCase):
    def setUp(self):
        print "preparation test %s" % self._testMethodName

    def tearDown(self):
        print "finish test %s" % self._testMethodName

    def test_sum_args(self):
        self.assertEqual(sum_args(1, 2, 3), 6)
        self.assertEqual(sum_args(1), 1)

    def test_sum_args_params(self):
        self.assertEqual(sum_args(*[1, 2, 3]), 6)


if __name__ == '__main__':
    unittest.main()