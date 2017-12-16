# -*- coding: utf-8 -*-

import unittest
from fn import * #导入所有待测试方法

#定义测试类
class TestFn(unittest.TestCase):

    # def setUp(self):
    #     print("这里是执行测试前的准备")

    # def tearDown(self):
    #     print("这里是测试完成后")

    @classmethod
    def setUpClass(cls):
        print("这里是执行测试前的准备")

    @classmethod
    def tearDownClass(cls):
        print("这里是测试完成后")

    def test_add(self):
        self.assertEqual(3, add(1,2))
    
    def test_minus(self):
        self.assertEqual(6, minus(7,1))

    def test_multi(self):
        self.assertEqual(6, multi(2,3))

    def test_divide(self):
        self.assertEqual(2,divide(6,3))
        self.assertEqual(2,divide(5,2))


#定义测试类
class TestFn2(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, add(1,2))
    


if __name__ == '__main__':
    unittest.main(verbosity=2)



