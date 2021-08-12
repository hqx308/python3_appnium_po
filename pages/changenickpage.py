#coding=utf-8
__author__ = 'hqx'

from selenium.webdriver.common.by import By
from pages import loginpage


class ChangeNick(loginpage.LoginOutPage):

	#----------------------------------------------以下是昵称修改相关元素
	#个人中心菜单，是一个list，在[4]的位置
	#引用Login_out的personhome4_loc
	#personhome4_loc=(By.ID,'com.alibaba.android.rimet:id/home_app_item')
	#点击头像进入信息设置界面
	avatar_loc = (By.ID, 'com.alibaba.android.rimet:id/iv_biz_card_avatar')

	#点击修改昵称
	nick_loc = (By.ID, 'com.alibaba.android.rimet:id/item_profile_nick')

	#输入要修改的昵称
	nickname_loc=(By.CLASS_NAME,'android.widget.EditText')

	# #点击确认修改&登出
	# surebutton_loc=(By.ID,'android:id/button1')

	#返回上一级
	back_loc=(By.CLASS_NAME,'android.widget.ImageButton')

	#-----------------------------------------以下是修改昵称相关操作
	#点击头像进入信息设置界面
	def click_avatar(self):
		self.clickButton(self.avatar_loc)

	#点击进行昵称修改
	def click_nick(self):
		self.clickButton(self.nick_loc)

	#输入昵称
	def input_nickname(self,name):
		self.send_keys(self.nickname_loc,name)

	# #点击确认修改&登出
	# def click_surebutton(self):
	# 	self.clickButton(self.surebutton_loc)

	#修改成功返回上一级
	def click_back(self):
		self.clickButton(self.back_loc)



