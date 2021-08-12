#coding=utf-8
__author__ = 'hqx'

import time

#登陆操作
def login(run,phone,code):
	try:
		run.input_phone(phone)
		run.input_code(code)
		run.click_privacy()
		run.click_login()
		run.mes_person()
		run.saveScreenshot('login')
		time.sleep(1)
	except Exception as e:
		print(e)

#登出操作
def logout(run):
	run.click_personhome4()
	run.click_setting7()
	run.click_signout()
	run.click_surebutton()
	time.sleep(1)
	run.mes_logout()
	time.sleep(1)



