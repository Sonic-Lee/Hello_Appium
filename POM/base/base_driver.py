# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------
# File       : base_driver.py
# Description: 初始化dirver对象
# Time       : 2020/7/15 14:12
# Author     : lijunpeng
# Email      : 18081876647@163.com
# Software   : PyCharm
# -------------------------------------------------------------------
from time import sleep
from appium import webdriver


def init_driver():
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
    desired_caps['appPackage'] = 'com.android.settings'
    # appActivity          启动的Activity
    desired_caps['appActivity'] = '.Settings'
    # unicodeKeyboard      unicode设置(允许中文输入)
    desired_caps['unicodeKeyboard'] = True
    # resetKeyboard        键盘设置(允许中文输入)
    desired_caps['resetKeyboard'] = True
    # 连接到appium服务端
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    sleep(1)
