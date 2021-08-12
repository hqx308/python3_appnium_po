#coding=utf-8
__author__ = 'hqx'

import time

#修改昵称
def changenick(run,name):
	try:
		#changenick_page = Change_Nick(LoginPage.driver)
		run.click_personhome4()
		time.sleep(1)
		run.click_avatar()
		run.click_nick()
		run.input_nickname(name)
		run.click_surebutton()
		run.saveScreenshot('nick')
		run.click_back()
		time.sleep(1)
	except Exception as e:
		print(e)

