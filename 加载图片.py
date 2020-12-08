import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.uic import loadUi
pic_path=['F:/austenite_boundary.bmp', 'F:/all_boundary.bmp', 'F:/bundary_density.png']
class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.i=0

    def mousePressEvent(self, e):
        print('mousePressEvent')
        if not len(pic_path):
            return
        self.i=(self.i+1)%len(pic_path)
        self.setPixmap(QPixmap(pic_path[self.i]))
        self.setScaledContents(True)

class CoreUI(QMainWindow):
    def __init__(self):
        super(CoreUI, self).__init__()
        loadUi('./Core.ui', self)
        # self.setWindowIcon(QIcon('./icons/icon.png'))
        # self.setFixedSize(1161, 623)
        self.runButton.clicked.connect(self.run)
        self.austcheckBox.stateChanged.connect(self.isSaveAust)
        self.allcheckBox.stateChanged.connect(self.isSaveALL)
        # self.lineEdit.
        self.boucheckBox.stateChanged.connect(self.isSaveBou)
        self.angcheckBox.stateChanged.connect(self.isSaveAng)
        self.picLabel = MyLabel(self.Box)
        self.picLabel.setGeometry(0, 20, 681, 480)
        self.picLabel.setPixmap(QPixmap("F:/austenite_boundary.bmp"))
    def isSaveAng(self,state):
        global isang
        if state == Qt.Checked:
            isang=True
        else:
            print('取消选中数据')
            isang=False
    def isSaveBou(self,state):
        global isbou
        if state == Qt.Checked:
            print('选中界面密度')
            isbou=True
        else:
            print('取消选中界面密度')
            isbou = False
    def isSaveALL(self,state):
        global isall
        if state == Qt.Checked:
            print('选中全部界面')
            isall=True
        else:
            print('取消选中全部界面')
            isall=False
    def isSaveAust(self,state):
        global isaust
        if state == Qt.Checked:
            print('选中奥体')
            isaust=True
        else:
            print('取消选中奥体')
            isaust = False
    def run(self):

        # print(data.step)

        pass
        # self.picLabel=MyLabel('1')
        # self.picLabel.setGeometry((0,20),681,480)
        # self.picLabel.setPixmap(QPixmap("F:/austenite_boundary.bmp"))

        # 图像捕获
        # self.isExternalCameraUsed = False
        # self.useExternalCameraCheckBox.stateChanged.connect(
        #     lambda: self.useExternalCamera(self.useExternalCameraCheckBox))
        # self.faceProcessingThread = FaceProcessingThread()
        # self.startWebcamButton.clicked.connect(self.startWebcam)
        #
        # # 数据库
        # self.initDbButton.setIcon(QIcon('./icons/warning.png'))
        # self.initDbButton.clicked.connect(self.initDb)
        #
        # self.timer = QTimer(self)  # 初始化一个定时器
        # self.timer.timeout.connect(self.updateFrame)
        #
        # # 功能开关
        # self.faceTrackerCheckBox.stateChanged.connect(
        #     lambda: self.faceProcessingThread.enableFaceTracker(self))
        # self.faceRecognizerCheckBox.stateChanged.connect(
        #     lambda: self.faceProcessingThread.enableFaceRecognizer(self))
        # self.panalarmCheckBox.stateChanged.connect(lambda: self.faceProcessingThread.enablePanalarm(self))

if __name__ == '__main__':
    # main()
    app = QApplication(sys.argv)
    window = CoreUI()
    window.show()
    sys.exit(app.exec())
