# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------
# File       : message_list_page.py
# Description: 
# Time       : 2020/7/15 14:32
# Author     : lijunpeng
# Email      : 18081876647@163.com
# Software   : PyCharm
# -------------------------------------------------------------------
from selenium.webdriver.common.by import By

from test.base.base_action import BaseAction


class MessageListPage(BaseAction):
    # 新建短信按钮
    new_massage_btn = By.ID, 'com.android.mms:id/action_compose_new'

    # 点击新建短信按键
    def page_click_new_massage(self):
        self.base_click(self.new_massage_btn)
