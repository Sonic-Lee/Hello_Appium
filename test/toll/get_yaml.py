# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------
# File       : get_yaml.py
# Description: 读取yaml文件数据
# Time       : 2020/7/15 17:02
# Author     : lijunpeng
# Email      : 18081876647@163.com
# Software   : PyCharm
# -------------------------------------------------------------------
import yaml

#读取yaml文件数据
def load_yaml_data(file_name):
    with open("../data/" + file_name + ".yaml", 'r',encoding='utf-8') as f:
        data = yaml.load(f)
        print(data)
        return data

#写入yaml文件数据
data={"list1":[{"name":"xiao","age":23},{"name":"xi","age":13},23,"hieh"],"list2":[{"name":"cao","age":33},{"name":"xa","age":11},24,"gff"]}
def dump_yaml_data(file_name):
    with open("../data/" + file_name + ".yaml", 'w',encoding='utf-8') as f:
        yaml.dump(data,f)

if __name__ == '__main__':
   # load_yml_data("data")
    load_yaml_data("xxx")
