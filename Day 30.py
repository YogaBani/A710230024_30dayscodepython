import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QScrollArea, QFileDialog, QMediaPlayer, QVideoWidget
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent

class TikTok(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("TikTok")
        self.setGeometry(300, 300, 400, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.header = QHBoxLayout()
        self.layout.addLayout(self.header)

        self.profileButton = QPushButton("Profile")
        self.header.addWidget(self.profileButton)

        self.uploadButton = QPushButton("Upload")
        self.header.addWidget(self.uploadButton)

        self.uploadButton.clicked.connect(self.uploadVideo)

        self.feed = QScrollArea()
        self.layout.addWidget(self.feed)

        self.feed.setWidgetResizable(True)

        self.feedContent = QWidget()
        self.feed.setWidget(self.feedContent)

        self.feedLayout = QVBoxLayout()
        self.feedContent.setLayout(self.feedLayout)

        self.videos = []

        self.show()

    def uploadVideo(self):
        videoDialog = VideoDialog(self)
        videoDialog.exec_()

    def addVideo(self, video):
        videoWidget = VideoWidget(video)
        self.feedLayout.addWidget(videoWidget)
        self.videos.append(videoWidget)

class VideoDialog(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Upload Video")
        self.setGeometry(300, 300, 300, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.videoLabel = QLabel("Video:")
        self.layout.addWidget(self.videoLabel)

        self.videoEdit = QLineEdit()
        self.layout.addWidget(self.videoEdit)

        self.browseButton = QPushButton("Browse")
        self.layout.addWidget(self.browseButton)

        self.browseButton.clicked.connect(self.browseVideo)

        self.captionLabel = QLabel("Caption:")
        self.layout.addWidget(self.captionLabel)

        self.captionEdit = QTextEdit()
        self.layout.addWidget(self.captionEdit)

        self.uploadButton = QPushButton("Upload")
        self.layout.addWidget(self.uploadButton)

        self.uploadButton.clicked.connect(self.uploadVideo)

    def browseVideo(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video", "", "Video Files (*.mp4 *.avi)")
        self.videoEdit.setText(filename)

    def uploadVideo(self):
        video = self.videoEdit.text()
        caption = self.captionEdit.toPlainText()
        videoData = {"video": video, "caption": caption}
        self.parent.addVideo(videoData)
        self.close()

class VideoWidget(QWidget):
    def __init__(self, video):
        super().__init__()

        self.video = video

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.videoPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()
        self.layout.addWidget(self.videoWidget)

        self.videoPlayer.setVideoOutput(self.videoWidget)

        self.videoPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.video["video"])))
        self.videoPlayer.play()

        self.captionLabel = QLabel(self.video["caption"])
        self.layout.addWidget(self.captionLabel)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tiktok = TikTok()
    sys.exit(app.exec_())
