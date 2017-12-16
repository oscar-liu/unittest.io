# -*- coding: utf-8 -*-

import unittest
from test_fn import TestFn
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    #实例化TestSuite
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFn))

    #将测试结果输出到文件中
    with open('HTMLReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)



