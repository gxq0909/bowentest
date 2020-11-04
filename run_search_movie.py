#!user/bin/python
#-*- coding:utf-8 -*-
# Author:高筱琪
# Dream
import unittest
import time
from config.HTMLTestRunner import HTMLTestRunner
# 找到要执行的测试用例的路径，和要执行的用例文件名字
discover = unittest.defaultTestLoader.discover(r'../test_case',pattern='search_movie_case.py')

if __name__ == '__main__':
    now = time.strftime('%Y%m%d%H%M%S')
    report_name = '../report//' + f'{now}.html'
    with open(report_name,'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                description='测试结果如下',
                                title='关键字检索电影测试报告',
                                tester='gxq',
                                verbosity=2)
        runner.run(discover)