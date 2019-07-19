#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: neo
# Date: 2019/2/22

###########################################################################
## Python code generated with wxFormBuilder (version Dec 17 2018)
###########################################################################

import wx
import wx.xrc

import threading
import queue

from killsp import Kill
from killsp import pyclip
from keylistener import KeyListener
from doConfig import ConfigProcessor

class MyFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "killsp", pos = wx.DefaultPosition,
                            size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        fgSizer = wx.FlexGridSizer( 1, 3, 0, 0 )
        fgSizer.SetFlexibleDirection( wx.BOTH )
        fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        bSizer = wx.BoxSizer( wx.VERTICAL )

        # 更新剪贴板内容
        self.btn_change = wx.Button( self, wx.ID_ANY, u"一键 kill sp", wx.DefaultPosition, (120,150), 0 )
        bSizer.Add( self.btn_change, 0, wx.ALL, 5 )

        # 实现格式转换
        self.btn_update = wx.Button( self, wx.ID_ANY, u"查看剪贴板内容", wx.DefaultPosition, (120,-1), 0 )
        bSizer.Add( self.btn_update, 0, wx.ALL, 5 )

        fgSizer.Add( bSizer, 1, wx.EXPAND, 5 )

        # 大文本框
        self.text_Paste = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, size=(400, 300),
                                       style=wx.TE_MULTILINE )
        fgSizer.Add( self.text_Paste, 0, wx.ALL, 5 )

        # 选择语言（处理的格式差异）
        languages = ["zh", "en"]
        self.radioLanguage = wx.RadioBox( self, wx.ID_ANY, u"选择语言",
                                          wx.DefaultPosition, (120, 20), languages, 3, wx.RA_SPECIFY_ROWS)
        bSizer.Add(self.radioLanguage, 0, wx.ALL, 5)

        self.SetSizer( fgSizer )
        self.Layout()

        self.statusBar = self.CreateStatusBar()

        self.Centre( wx.BOTH )

    def __del__(self):
        pass


class MainWindow(MyFrame):
    def __init__(self, parent):
        MyFrame.__init__(self, parent)
        self.dataQueue = queue.Queue()

        # 绑定控件事件处理器
        self.Bind(wx.EVT_BUTTON, self.onUpdateBtn, self.btn_update)
        self.Bind(wx.EVT_BUTTON, self.onChangeBtn, self.btn_change)

        self.radioLanguage.Bind(wx.EVT_RADIOBOX, self.onCheckLanguage)
        # 读取现在配置文件中的配置，初始化
        processor = ConfigProcessor()
        lang = processor.readConfig()
        self.radioLanguage.SetSelection(self.radioLanguage.FindString(lang))

        # 启动键盘监听线程
        self.keyThread = KeyboardThread()
        self.keyThread.setDaemon(True)
        self.keyThread.start()

    def onUpdateBtn(self, event):
        """
        把现在剪贴板的内容显示出来
        """
        self.text_Paste.Clear()
        clip = pyclip.paste()
        print(clip)
        self.text_Paste.write(clip)


    def onChangeBtn(self, event):
        """
        一键处理剪贴板的内容
        """
        self.text_Paste.Clear()
        kill = Kill()
        sout = kill.kill_sp()
        print(sout)
        self.text_Paste.write(sout)

    def onCheckLanguage(self, event):
        """
        接收单选框的字符串，并写入配置文件
        设置处理的格式
        """
        lang = self.radioLanguage.GetStringSelection()
        processor = ConfigProcessor()
        processor.setCongfig(lang)




class KeyboardThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        listener = KeyListener()
        listener.start()


# 主程序
if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None)
    frame.Show()
    app.MainLoop()