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


class TestLogout:
    #预计成功，实际成功
    @pytest.mark.xfail(condition=False, reason="预计成功，实际成功")
    def test_03(self):
        print('test3')
        assert 1

    # 预计失败，实际成功
    @pytest.mark.xfail(condition=True, reason="预计失败，实际成功")
    def test_04(self):
        print('test4')
        assert 1

    # 预计失败，实际失败
    @pytest.mark.xfail(condition=True, reason="预计失败，实际失败")
    def test_05(self):
        print('test5')
        assert 0


    # 预计成功，实际失败
    @pytest.mark.xfail(condition=False, reason="预计成功，实际失败")
    def test_06(self):
        print('test6')
        assert 0

if __name__ == '__main__':
    pytest.main(['-s', "test_logout.py"])
