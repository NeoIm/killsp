##### Author：neo

这是一个小小小程序，用于清理pdf复制出来的嵌有大量空格和回车的文字

开发环境：python 3.6
建议也在同样的环境下运行

### v1.0
使用str的replace函数
暂时不能处理分段文字，全部内容会生成在一个段里

### v1.1
直接从剪贴板输入，并输出到剪贴板

### v2.0
请下载killsp.py和ui.py到同一目录下。  
加入了ui模块，在命令行运行 `python ui.py` 即可运行本程序。  
界面十分小巧简单，把需要处理的文字复制到剪贴板之后，点击一键处理就可以了，处理好的文字内容仍在剪贴板内，可以通过右边窗口预览。
