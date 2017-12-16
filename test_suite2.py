# -*- coding: utf-8 -*-

import unittest
from test_fn import TestFn

if __name__ == '__main__':
    #实例化TestSuite
    suite = unittest.TestSuite()

    #直接用addTest方法添加单个TestCase
    suite.addTest(TestFn('test_add'))

    #用addTest + TestLoader

    #loadTestsFromName(), 传入'模块名,TestCase名'
    suite.addTests(unittest.TestLoader().loadTestsFromName('test_fn.TestFn'))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

