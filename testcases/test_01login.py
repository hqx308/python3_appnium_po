# -*- coding: utf-8 -*-
__author__ = 'hqx'
import unittest
import parameterized
from appium import webdriver
from pages import loginpage
from PO import baselogin
from pages.loginpage import basemethod

class Login(unittest.TestCase):

	def setUp(self):
		# 可以进行参数化的初始化操作
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', basemethod.Base.capabilities)
		self.run = loginpage.LoginOutPage(self.driver)
		# pass
		# self.phone=18xxxxxxxx
		# self.code='xxxxxxxxxx'

	#账号密码要输入可以登录的
	@parameterized.parameterized.expand([(18000000000,'xxxxxx'),(18000000000,'xxxxx')])
	def test_login(self,phone,code):
		u'''测试钉钉登陆功能'''
		baselogin.login(self.run,phone, code)

	def tearDown(self):
		baselogin.logout(self.run)
		self.driver.quit()
		# pass

if __name__ == '__main__':
	unittest.main()

