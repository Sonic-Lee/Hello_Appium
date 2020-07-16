# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------
# File       : test_login.py
# Description: 
# Time       : 2020/7/14 13:24
# Author     : lijunpeng
# Email      : 18081876647@163.com
# Software   : PyCharm
# -------------------------------------------------------------------
import pytest


class TestLogin:
    @pytest.mark.run(order=-2)
    def test_01(self):
        print('test1')
        assert 1

    @pytest.mark.run(order=-1)
    def test_02(self):
        print('test2')
        assert 0



if __name__ == '__main__':

    pytest.main(['-s', "test_login.py"])
