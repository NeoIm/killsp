#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: neo
# Date: 2018/11/30
# Modify: 2019/2/22

import pyperclip as pyclip

from doConfig import ConfigProcessor

'''
删掉一段文字内的空格和回车
解决pdf中复制出的文字问题
'''
class Kill:
    def __init__(self):
        # 输入、输出的文件路径
        self.filename = 'sin.txt'
        self.outfilename = 'sout.txt'

    def kill_sp(self):
        # 获取剪贴板上的文字
        self.sin = pyclip.paste()
        self.sout = self.sin

        # 根据配置文件的语言选择处理的方式
        processor = ConfigProcessor()
        lang = processor.readConfig()
        if(lang == processor.valueZh):
            self.sout = self.sin.replace(' ', '').replace('\n', '').replace('\r', '')
        elif(lang == processor.valueEn):
            self.sout = self.sin.replace('\n', ' ').replace('\r', '')

        # 处理好的文字放回剪贴板
        pyclip.copy(self.sout)

        print('input:  ', self.sin)
        print('output: ', self.sout)

        return self.sout

    def save(self):
        # 保存到txt文件
        with open(outfilename, 'w', encoding="utf-8") as out:
            out.write(self.sout)




if __name__ == "__main__":
    # 搜索根目录下的sin.txt文件，要提前把要转换的文字保存在里面
    # sin = str input
    filename = 'sin.txt'
    outfilename = 'sout.txt'

    # 输入的字符串
    # sin = None
    # with open(filename, 'r', encoding="utf-8") as f:
        # sin = f.read()
    # sin = input('input the str')

    # 输入从剪贴板取数据
    sin = pyclip.paste()

    # 把输入字符串的空格和回车删除
    sout = sin.replace(' ', '').replace('\n', '').replace('\r', '')
    # sout = sin.replace('\n', ' ').replace('\r', '')

    # 打印输入和输出的文字内容，供再复制
    print("sin: ", sin)
    print("sout: ", sout)

    # 保存到txt文件
    with open(outfilename, 'w', encoding="utf-8") as out:
        out.write(sout)

    # 将文字写入剪贴板
    pyclip.copy(sout)

