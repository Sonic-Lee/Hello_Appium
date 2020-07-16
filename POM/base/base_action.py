# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------
# File       : base_action.py
# Description: base类，封装Appium底层方法
# Time       : 2020/7/15 13:35
# Author     : lijunpeng
# Email      : 18081876647@163.com
# Software   : PyCharm
# -------------------------------------------------------------------


# base类
from selenium.webdriver.support.wait import WebDriverWait

from POM.base.base_driver import init_driver


class BaseAction:

    def __init__(self):
        self.driver = init_driver()

    # 查找一个元素方法
    def base_find_element(self, loc, timeout=10, poll=0.5):
        """
        使用显示等待 查找元素
        :param timeout:找找元素的等待时间，默认10秒
        :param poll:查找元素的频率，默认0.5秒
        :param loc:传入的元素查找对象，传入一个元祖
        :return:元素
        """
        try:
            element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                lambda x: x.find_element(*loc))
            return element
        except Exception as e:
            print(e)

    # 查找同类元素方法
    def base_find_elements(self, loc, timeout=10, poll=0.5):
        """
               使用显示等待 查找元素
               :param timeout:
               :param poll:
               :param loc:
               :return:
               """
        try:
            elements = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                lambda x: x.find_elements(*loc))
            return elements
        except Exception as e:
            print(e)

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 获取文本信息
    def base_get_text(self, loc):
        self.base_find_element(loc)

    # 输入方法
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find_element(loc)
        # 清除文本框
        el.clear()
        # 输入
        el.sendkey(value)
