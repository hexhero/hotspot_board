# _*_ coding:utf-8 _*_
'''
作者：杨斌
创建日期: 2023/9/21
描述: 热点面板
Python版本: 3.x
'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMenu, QSystemTrayIcon,QAction
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import sys, random
import data
import filepath

icon_path = filepath.resource_path("icon.png")

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(120, 120, 800, 300) # x, y, w, h
        self.label = QLabel('Hotspot board.', self, styleSheet='color: yellow; font-size: 18px; font-weight: bold;')
        self.label.setFixedWidth(self.width() - 20)
        self.label.move(10, 10)
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)
        
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
        
        # 显示图片
        # self.imglabel = QLabel(self)
        # icon = QPixmap('img.png')
        # icon = icon.scaled(100, 100)
        # self.imglabel.setPixmap(icon)
        # self.imglabel.move(0, 0)
    
        # 定时刷新
        self.refresh()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000 * 60)
        
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
    def refresh(self):
        # usdcnh = data.getUSDCNH()
        ss, usdcnh = data.getAll()
        self.label.setText(f'USDCNH: {usdcnh[2]}/{usdcnh[3]}\nSS: {ss[2]}/{round(ss[4], 2)}')
        # self.showMessage('热点面板', f'USDCNH: {usdcnh[2]}/{usdcnh[3]}\nSS: {ss[2]}/{round(ss[4], 2)}', QSystemTrayIcon.Information)
        
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
            self.timer.stop()
            self.quit_application()
            
if __name__ == '__main__':
    print(__doc__)
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())