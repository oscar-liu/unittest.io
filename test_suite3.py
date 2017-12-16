# -*- coding: utf-8 -*-

import unittest
from test_fn import TestFn,TestFn2

if __name__ == '__main__':
    #实例化TestSuite
    suite = unittest.TestSuite()

    #直接用addTest方法添加单个TestCase
    suite.addTest(TestFn('test_add'))

    #用addTest + TestLoader

    #loadTestsFromName(), 传入'模块名,TestCase名'

    # loadTestsFromNames加入list中
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_fn.TestFn','test_fn.TestFn2']))


    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

