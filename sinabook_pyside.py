# coding=utf-8

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtWebKit import *


if __name__ == '__main__':

    url = "http://book.sina.com.cn/excerpt/rwws/"

    app = QApplication([])  # 完成其他Qt对象之前，必须先创建该对象
    webview = QWebView()  # 该对象是Web 对象的容器

    # 调用show方法显示窗口
    # webview.show()

    # 设置循环事件， 并等待网页加载完成
    loop = QEventLoop()
    webview.loadFinished.connect(loop.quit)
    webview.load(QUrl(url))
    loop.exec_()

    frame = webview.page().mainFrame()  # QWebFrame类有很多与网页交互的有用方法

    # 得到渲染后页面的html代码
    html = frame.toHtml()

    print html

