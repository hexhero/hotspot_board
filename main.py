from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMenu
from PyQt5 import QtCore
import sys, random
import data

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
        # 定时刷新
        self.refresh()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000 * 30)
        
        # 显示图片
        # self.imglabel = QLabel(self)
        # icon = QPixmap('img.png')
        # icon = icon.scaled(100, 100)
        # self.imglabel.setPixmap(icon)
        # self.imglabel.move(0, 0)
    
    
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
        self.label.setText(f'USDCNH: {usdcnh[2]}\nSS: {ss[2]}');
        
    # 右键菜单
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        exitAct = cmenu.addAction("Exit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == exitAct:
            self.timer.stop()
            self.close()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())