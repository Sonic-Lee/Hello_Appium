# -*- coding：utf-8-*-#

# -------------------------------------------------------------------------------
# Name:         demo
# Description:
# Author:       Administrator
# Date:         2020/7/13
# -------------------------------------------------------------------------------
from time import sleep
from appium import webdriver

# desired_caps：负责启动server服务端时的参数设置，
# appium server 与手机端建立会话关系时，根据这些参数服务端可以做出相应的处理
desired_caps = dict()
#  platformName       平台的名称：iOS, Android, or FirefoxOS
desired_caps['platformName'] = 'Android'
# platformVersion      设备系统版本号
desired_caps['platformVersion'] = '5.1'
# deviceName           设备号 IOS：instruments -s devices，Android: adb devices 安卓可以随意修改，但不能为空
desired_caps['deviceName'] = '192.168.180.101:5555'
# appPackage           启动的包
desired_caps['appPackage'] = 'com.android.mms'
# appActivity          启动的Activity
desired_caps['appActivity'] = '.ui.ConversationList'
# unicodeKeyboard      unicode设置(允许中文输入)
desired_caps['unicodeKeyboard'] = True
# resetKeyboard        键盘设置(允许中文输入)
desired_caps['resetKeyboard'] = True
# 连接到appium服务端
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(1)
# # 跳转到短信页面
# driver.start_activity("com.android.mms", '.ui.ConversationList')
# # 退出app
# driver.close_app()
# # 输出当前程序的包名
# print(driver.current_package)
# # 输出当前程序的包名
# print(driver.current_activity)
# sleep(5)
# driver.is_app_installed("com.android.mms")
# # driver.quit()

# driver.background_app(5)
driver.find_element_by_id('com.android.mms:id/action_compose_new').click()
sleep(2)
driver.find_element_by_id('com.android.mms:id/recipients_editor').send_keys("12311112222")
driver.find_element_by_id('com.android.mms:id/embedded_text_editor').send_keys("dddd")
driver.find_element_by_id('com.android.mms:id/send_button_sms').click()
sleep(5)
