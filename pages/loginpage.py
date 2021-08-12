#coding=utf-8
__author__ = 'hqx'

from selenium.webdriver.common.by import By
from common import basemethod

'''
钉钉登陆页面涉及的页面元素 - 操作方法 -> 封装
'''

class LoginOutPage(basemethod.Base):

	#----------------------------------------------以下是登陆相关元素
	#电话输入框
	phoneinput_loc=(By.ID,'com.alibaba.android.rimet:id/et_phone_input')

	#密码输入框
	codeinput_loc = (By.ID, 'com.alibaba.android.rimet:id/et_pwd_login')

	#保密协议确认钮
	privacy_loc = (By.ID, 'com.alibaba.android.rimet:id/cb_privacy')

	#登陆按钮
	login_loc=(By.ID,'com.alibaba.android.rimet:id/tv')

	#登陆成功后显示个人信息
	person_loc=(By.ID,'com.alibaba.android.rimet:id/fl_avatar')

	#-----------------------------------------以下是登陆相关操作
	#输入电话号码
	def input_phone(self,phone):
		self.send_keys(self.phoneinput_loc,phone)

	#输入密码
	def input_code(self,code):
		self.send_keys(self.codeinput_loc,code)

	#点击保密协议按钮
	def click_privacy(self):
		self.clickButton(self.privacy_loc)

	#点击登陆按钮
	def click_login(self):
		self.clickButton(self.login_loc)

	#登陆成功后显示个人信息
	def mes_person(self):
		els = self.find_element(self.person_loc)
		#recipe_list = json.dumps(list, encoding='UTF-8', ensure_ascii=False)
		#我的信息
		print(u'登陆成功个人信息展示:'+els.tag_name)


	#---------------------------------------------以下是登出相关元素
	#个人中心菜单，是一个list，在[4]的位置
	personhome4_loc=(By.ID,'com.alibaba.android.rimet:id/home_app_item')

	#设置按钮，List，在[7]的位置
	setting7_loc=(By.ID,'com.alibaba.android.rimet:id/content_container')

	#登出按钮
	signout_loc=(By.ID,'com.alibaba.android.rimet:id/setting_sign_out')

	#登出确认按钮
	surebutton_loc=(By.ID,'android:id/button1')

	#------------------------------------以下是登出操作
	#点击到个人中心
	def click_personhome4(self):
		self.clickButtons(self.personhome4_loc,4)

	#点击设置按钮
	def click_setting7(self):
		self.clickButtons(self.setting7_loc,7)

	#点击登出按钮
	def click_signout(self):
		self.clickButton(self.signout_loc)

	#点击登出确认按钮
	def click_surebutton(self):
		self.clickButton(self.surebutton_loc)

	#登出成功后，返回登录界面
	def mes_logout(self):
		els = self.find_element(self.login_loc)
		#我的信息
		print(u'登出后信息展示:'+els.text)




