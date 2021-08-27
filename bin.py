from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from GUI import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtMultimedia import QMediaPlaylist
from myVideoWidget import myVideoWidget
from testhr import *
from take_photo import *
import sys


class myMainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()#继承Ui_MainWindow类
        self.setupUi(self)#界面初始化
        self.videoFullScreen = False   # 判断当前widget是否全屏
        self.videoFullScreenWidget = myVideoWidget()   # 创建一个全屏的widget
        self.videoFullScreenWidget.setFullScreen(1)
        self.videoFullScreenWidget.hide()               # 不用的时候隐藏起来
        self.playlist = QMediaPlaylist(self)
        self.player = QMediaPlayer()  #播放器线程
        self.player.setPlaylist(self.playlist)
        self.player.setVideoOutput(self.wgt_video)  # 视频播放输出的widget，就是上面定义
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)  # 3
        self.playlist.setCurrentIndex(2)  # 4

        self.btn_open.clicked.connect(self.openVideoFile)   # 打开视频文件按钮
        self.btn_play.clicked.connect(self.playVideo)       # play
        self.btn_stop.clicked.connect(self.pauseVideo)       # pause
        self.player.positionChanged.connect(self.changeSlide)      # change Slide
        self.sld_video.sliderMoved.connect(self.slider_change)     #拖进度条
        self.videoFullScreenWidget.doubleClickedItem.connect(self.videoDoubleClicked)  #双击响应
        self.wgt_video.doubleClickedItem.connect(self.videoDoubleClicked)   #双击响应

        #满载部分
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.getdatastart)
        self.work=WorkThread()#实例化一个线程
        self.work.trigger.connect(self.distance)
        self.getdate.clicked.connect(self.getdatastart) # 绑定点击事件函数
        self.stopgetdate.clicked.connect(self.timerstop)  # 绑定点击事件函数

        #显示垃圾


        self.timer2=QTimer(self)
        self.timer2.timeout.connect(self.getdatastart2)
        self.work2=Phototake()
        self.work2.trigger2.connect(self.photoresult)#结果
        self.photostart.clicked.connect(self.beginrun)
        self.photostop.clicked.connect(self.stoprun)



    def getdatastart(self):
            self.timer.start(500)
            self.work.start()
        #开启定时器
    def timerstop(self):
            print('stop')
            #self.distanceEdit.setText('stop')
        # 关闭定时器
            self.timer.stop()

    def distance(self):
        hr2 = hrsr04()
        a = hr2.checkdist()
        if(a>=99):
            w=99#垃圾桶满载高度
        else:
            w=a
        m=99-int(w)
        time = QTime.currentTime()
        t = time.toString()  # 时间
        print(t + ':    %0.2f cm' % m)
        self.progressBar.setValue(int(m))  # 显示距离

    #显示垃圾

    def beginrun(self):
        self.timer2.start(500)
        self.work2.start()

    def stoprun(self):
        print('stop')
        # self.distanceEdit.setText('stop')
        # 关闭定时器
        self.timer2.stop()

    def photoresult(self):
        po=photoclass()
        b=po.takephoto()
        if b==None:
            print("no trash")
        else:
            for i,element in b:
                self.textEdit.setPlainText(self.textEdit.toPlainText()+"trash"+(i+1)+"is"+element)







    #播放部分：
    def openVideoFile(self):
        self.playlist.addMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件
        self.player.play()  # 播放视频
    def playVideo(self):
        self.player.play()
    def pauseVideo(self):
        self.player.pause()



    def changeSlide(self,position):
        self.videoLength = self.player.duration()+0.1
        self.sld_video.setValue(round((position/self.videoLength)*100))
        self.lab_video.setText(str(round((position/self.videoLength)*100,2))+'%')

    def slider_change(self):
        self.videoLength2 = self.player.duration()
        self.player.setPosition(float(self.sld_video.value()/100*self.videoLength2))


    def videoDoubleClicked(self,text):
        if self.player.duration() > 0:  # 开始播放后才允许进行全屏操作
            if self.videoFullScreen:
                self.player.pause()
                self.videoFullScreenWidget.hide()
                self.player.setVideoOutput(self.wgt_video)
                self.player.play()
                self.videoFullScreen = False
            else:
                self.player.pause()
                self.videoFullScreenWidget.show()
                self.player.setVideoOutput(self.videoFullScreenWidget)
                self.player.play()
                self.videoFullScreen = True


class WorkThread(QThread):
    # 定义一个信号
    trigger = pyqtSignal()

    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def run(self):
        # 触发信号
        self.trigger.emit()
class Phototake(QThread):
    trigger2=pyqtSignal()
    def __init__(self):
        super(Phototake, self).__init__()
    def run2(self):
        self.trigger2.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = myMainWindow()
    vieo_gui.show()
    hr = hrsr04()
    hr.inithr()
    sys.exit(app.exec_())