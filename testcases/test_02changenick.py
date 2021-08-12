# -*- coding: utf-8 -*-
__author__ = 'hqx'
import unittest
from PO import changenick
import parameterized
from appium import webdriver
from PO import baselogin
from pages import changenickpage
from pages.changenickpage import loginpage

class TestChangeNick(unittest.TestCase):

	def setUp(self):
		#参数初始化
		# pass
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', loginpage.basemethod.Base.capabilities)
		self.run = changenickpage.ChangeNick(self.driver)
		self.phone=18000000000  #手机号要输入可以登录的手机号
		self.code='xxxxxx'	#密码要输入正确密码
		# self.name='hqx'

	#昵称参数化
	@parameterized.parameterized.expand([('hqx'),('何其晓'),('hqx123'),('hqxtest')])
	def test_changenick(self, name):
		u'''钉钉登陆'''
		baselogin.login(self.run,self.phone, self.code)
		u'''修改昵称'''
		changenick.changenick(self.run,name)


	def tearDown(self):
		u'''钉钉登出'''
		baselogin.logout(self.run)
		self.driver.quit()
		#pass

if __name__ == '__main__':
	unittest.main()

