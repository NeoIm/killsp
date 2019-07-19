#### Author：neo
#### Email：ligao36@163.com

这是一个小小小程序，用于清理pdf复制出来的嵌有大量空格和回车的文字  
后续考虑添加针对md公式（识别\符号避免md格式出错）等功能，希望有其他细化功能的欢迎邮件指点

开发环境：python 3.6 + Win10
建议也在同样的环境下运行，Mac也可，Linux未测试

### 使用说明
0. 安装python 3.6或以上版本

1. 请下载killsp.py、ui.py、keyboard.py、doConfig.py到同一目录下。（打包下载就对了）
在命令行运行 `python ui.py` 即可运行本程序，会显示一个小窗口。  
在window下，双击`ui.py`也可以直接运行

2. 需要的第三方包：（均pip即可下载）
* wx：界面程序              pip install -U wxPython
* pyperclip：剪贴板处理     pip install pyperclip  
* pynput：键盘监听          pip install pynput

### 最新版本 v3.0
增加英文内容的格式支持，其实就是删掉回车加一个空格
增加了配置文件（config.ini），用于保存当前处理格式

### v1.0
使用str的replace函数
暂时不能处理分段文字，全部内容会生成在一个段里

### v1.1
直接从剪贴板输入，并输出到剪贴板

### v2.0
加入了ui模块，有一个小窗口。
界面十分小巧简单，把需要处理的文字复制到剪贴板之后，点击一键处理就可以了，处理好的文字内容仍在剪贴板内，可以通过右边窗口预览。

### v2.1
加入了键盘监听模块，仍是运行`python ui.py` 主程序  
点击ctrl + alt + c 即可处理剪贴版中的内容

### v3.0
增加英文内容的格式支持，其实就是删掉回车加一个空格
增加了配置文件（config.ini），用于保存当前处理格式
