# -*- coding: utf-8 -*-

import unittest
from test_fn import TestFn

if __name__ == '__main__':
    #实例化TestSuite
    suite = unittest.TestSuite()

    #将测试方法按照顺序加入到list
    tests = [ TestFn('test_add'), TestFn('test_minus'), TestFn('test_multi'), TestFn('test_divide') ]
    #添加到TestSuite中
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


