# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------
# File       : new_message_page.py
# Description: 新建短信页面
# Time       : 2020/7/15 14:39
# Author     : lijunpeng
# Email      : 18081876647@163.com
# Software   : PyCharm
# -------------------------------------------------------------------
from time import sleep

from selenium.webdriver.common.by import By

from test.base.base_action import BaseAction


class NewMessagePage(BaseAction):
    # 接收者输入框
    recipients_editor = By.ID, 'com.android.mms:id/recipients_editor'
    # 信息输入框
    EditText = By.ID, 'com.android.mms:id/embedded_text_editor'
    # 发送短信按键
    send_button_sms = By.ID = 'com.android.mms:id/send_button_sms'

    # 输入接收人电话
    def input_recipients(self, recipient):
        self.base_input(self.recipients_editor, recipient)

    # 输入信息文本
    def input_message_text(self, message_text):
        self.base_input(self.EditText, message_text)


    # 点击发送短信按键
    def click_send_message(self):
        self.base_click(self.send_button_sms)
