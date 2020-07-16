# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------
# File       : test_message.py
# Description: 测试短信发送功能
# Time       : 2020/7/15 14:49
# Author     : lijunpeng
# Email      : 18081876647@163.com
# Software   : PyCharm
# -------------------------------------------------------------------
from time import sleep

import appium

import pytest

from test.base.base_driver import init_driver
from test.page.page import Page


class TestMessage:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    # @pytest.mark.parametrize(("phone", "content"), [('18088888888', 'hello'), ('13011111111', 'world')])
    def test_send_message(self):
        # 主页新建短信
        self.page.message_list.page_click_new_massage()

        # 新建短信--输入接收人
        self.page.new_massage.input_recipients("13011112222")

        # 新建短信--输入文本
        self.page.new_massage.input_message_text("content")
        sleep(3)

        # 新建短信--点击发送
        self.page.new_massage.click_send_message()
