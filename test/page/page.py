# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------
# File       : page.py
# Description: page入口
# Time       : 2020/7/15 14:53
# Author     : lijunpeng
# Email      : 18081876647@163.com
# Software   : PyCharm
# -------------------------------------------------------------------
from test.page.message_list_page import MessageListPage
from test.page.new_message_page import NewMessagePage


class Page:

    def __init__(self,driver):
        self.driver=driver

    @property
    def message_list(self):
        return MessageListPage(self.driver)

    @property
    def new_massage(self):
        return NewMessagePage(self.driver)