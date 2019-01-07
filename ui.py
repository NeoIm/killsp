# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Dec 17 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        fgSizer = wx.FlexGridSizer( 1, 3, 0, 0 )
        fgSizer.SetFlexibleDirection( wx.BOTH )
        fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.textCopy = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer.Add( self.textCopy, 0, wx.ALL, 5 )

        bSizer = wx.BoxSizer( wx.VERTICAL )

        self.btn_update = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.btn_update, 0, wx.ALL, 5 )

        self.btn_change = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.btn_change, 0, wx.ALL, 5 )

        self.m_button10 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.m_button10, 0, wx.ALL, 5 )


        fgSizer.Add( bSizer, 1, wx.EXPAND, 5 )

        self.text_Paste = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer.Add( self.text_Paste, 0, wx.ALL, 5 )


        self.SetSizer( fgSizer )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__(self):
        pass

# 主程序
if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame1(None)
    # frame.statusBar.SetStatusText('program started')
    frame.Show()
    app.MainLoop()