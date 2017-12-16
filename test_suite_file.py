# -*- coding: utf-8 -*-

import unittest
from test_fn import TestFn

if __name__ == '__main__':
    #实例化TestSuite
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFn))

    #将测试结果输出到文件中
    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suite)


