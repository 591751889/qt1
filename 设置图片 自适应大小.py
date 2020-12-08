import sys

from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget, QApplication

class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)


    def mousePressEvent(self,e):
        print('mousePressEvent')



class Test(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置布局
        myLayout = QGridLayout()
        # 设置布局没有边缘空白
        myLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(myLayout)
        t = MyLabel("test")
        # 设置图片
        t.setPixmap(QPixmap("F:/austenite_boundary.bmp"))
        t.setScaledContents(True)
        # 设置label最大大小
        t.setMaximumSize(680, 480)

        myLayout.addWidget(t)

        # self.setGeometry(300, 200, 550, 550)




        self.show()

    def hide_self(self):
            print('k')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    sys.exit(app.exec_())
