#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: neo
# Date: 2018/11/30

'''
删掉一段文字内的空格和回车
解决pdf中复制出的文字问题
'''


if __name__ == "__main__":
    # 搜索根目录下的sin.txt文件，要提前把要转换的文字保存在里面
    # sin = str input
    filename = 'sin.txt'
    outfilename = 'sout.txt'

    # 输入的字符串
    sin = None
    with open(filename, 'r', encoding="utf-8") as f:
        sin = f.read()
    # sin = input('input the str')

    # 把输入字符串的空格和回车删除
    sout = sin.replace(' ', '').replace('\n', '')

    # 打印输入和输出的文字内容，供再复制
    print("sin: ", sin)
    print("sout: ", sout)

    # 保存到txt文件
    with open(outfilename, 'w', encoding="utf-8") as out:
        out.write(sout)


