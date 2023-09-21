# _*_ coding:utf-8 _*_
'''
作者：杨斌
创建日期: 2023/9/21
描述: 热点面板
Python版本: 3.x
'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMenu, QSystemTrayIcon, QAction, QHBoxLayout, QVBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sys
import data as ddd
import filepath

icon_path = filepath.resource_path("icon.png")

class UI(QWidget):
    
    themes = {
        'spring': ['#ebeee8', '#d2af9d', '#ea5514', '#3271ae'],
        'yushui': ['#f9d3e3', '#beb1aa', '#e5a84b', '#c0d695']
    }
    
    def __init__(self, theme='spring'):
        super().__init__()
        self.theme = UI.themes.get(theme,'spring')
        self.initUI()

    def initUI(self):
        # 设置全局字体
        font = QFont()
        font.setFamily('Microsoft YaHei UI')
        self.setFont(font)
        # 设置窗口样式
        self.setWindowFlags(self.windowFlags(
        ) | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(120, 120, 300, 300)  # x, y, w, h
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)
        # 初始化布局
        self.init_layout()
        # 初始化系统托盘
        self.init_tray()
        # 初始化任务
        self.init_task()

    def init_task(self):
        # 定时刷新
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.refresh_ui)
        self.timer.start(1000 * 60)

    def init_tray(self):
        # 设置系统托盘
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(icon_path))
        # 创建托盘菜单
        self.tray_menu = QMenu()
        self.show_action = QAction("Show", self)
        self.quit_action = QAction("Exit", self)
        self.tray_menu.addAction(self.show_action)
        self.tray_menu.addAction(self.quit_action)
        # 将托盘菜单设置给托盘图标
        self.tray_icon.setContextMenu(self.tray_menu)
        # 连接信号槽
        self.show_action.triggered.connect(self.show)
        self.quit_action.triggered.connect(self.quit_application)
        # 显示托盘图标
        self.tray_icon.show()

    def init_layout(self):
        self.refresh_data()
        self.labels = []
        wrap = QVBoxLayout()
        wrap.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        for d1 in self.data:
            line = QHBoxLayout()
            line.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            subLabel = []
            for i, d2 in enumerate(d1):
                clr = self.theme[i] if i < len(self.theme) else '#green'
                label = QLabel(d2, self, styleSheet=f'color: {clr}; font-size: 14px; font-weight: bold;')
                line.addWidget(label)
                subLabel.append(label)
            wrap.addLayout(line)
            self.labels.append(subLabel)
        self.setLayout(wrap)

    # 关闭事件最小化到托盘
    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            '热点面板',
            '已最小化到托盘',
            QSystemTrayIcon.Information,
            2000
        )

    def quit_application(self):
        self.tray_icon.hide()
        QApplication.quit()

    # 鼠标拖拽效果
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = None
            event.accept()
    
    # 刷新数据
    def refresh_data(self):
        self.data = ddd.getData()

    def refresh_ui(self):
        self.refresh_data()
        for i,v in enumerate(self.data):
            labels = self.labels[i]
            for i2,v2 in enumerate(v):
                labels[i2].setText(str(v2))
    
    # 显示系统消息
    # def showMessage(self, title, message, icon):
    #     if icon is None: icon = QSystemTrayIcon.Information
    #     self.tray_icon.showMessage(title, message, icon, 2000)

    # 右键菜单
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        exitAct = cmenu.addAction("Exit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == exitAct:
            # self.timer.stop()
            self.quit_application()


if __name__ == '__main__':
    print(__doc__)
    app = QApplication(sys.argv)
    ui = UI(theme='yushui')
    ui.show()
    sys.exit(app.exec_())
