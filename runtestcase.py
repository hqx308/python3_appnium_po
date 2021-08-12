#!/usr/bin/python3
# _*_ coding:utf-8 _*_
__author__ = 'hqx'

import unittest
from report.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite=unittest.defaultTestLoader.discover('',pattern='test_*')
    htmlreport=open('./test.html', 'wb')
    runner=HTMLTestRunner(stream=htmlreport,title='测试报告',description='测试描述',tester='hqx')
    runner.run(suite)
    htmlreport.close()