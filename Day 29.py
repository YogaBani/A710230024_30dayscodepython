import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QScrollArea, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class Instagram(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Instagram")
        self.setGeometry(300, 300, 400, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.header = QHBoxLayout()
        self.layout.addLayout(self.header)

        self.profileButton = QPushButton("Profile")
        self.header.addWidget(self.profileButton)

        self.postButton = QPushButton("Post")
        self.header.addWidget(self.postButton)

        self.postButton.clicked.connect(self.createPost)

        self.feed = QScrollArea()
        self.layout.addWidget(self.feed)

        self.feed.setWidgetResizable(True)

        self.feedContent = QWidget()
        self.feed.setWidget(self.feedContent)

        self.feedLayout = QVBoxLayout()
        self.feedContent.setLayout(self.feedLayout)

        self.posts = []

        self.show()

    def createPost(self):
        postDialog = PostDialog(self)
        postDialog.exec_()

    def addPost(self, post):
        postWidget = PostWidget(post)
        self.feedLayout.addWidget(postWidget)
        self.posts.append(postWidget)

class PostDialog(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Create Post")
        self.setGeometry(300, 300, 300, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.imageLabel = QLabel("Image:")
        self.layout.addWidget(self.imageLabel)

        self.imageEdit = QLineEdit()
        self.layout.addWidget(self.imageEdit)

        self.browseButton = QPushButton("Browse")
        self.layout.addWidget(self.browseButton)

        self.browseButton.clicked.connect(self.browseImage)

        self.captionLabel = QLabel("Caption:")
        self.layout.addWidget(self.captionLabel)

        self.captionEdit = QTextEdit()
        self.layout.addWidget(self.captionEdit)

        self.postButton = QPushButton("Post")
        self.layout.addWidget(self.postButton)

        self.postButton.clicked.connect(self.createPost)

    def browseImage(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.jpg *.png)")
        self.imageEdit.setText(filename)

    def createPost(self):
        image = self.imageEdit.text()
        caption = self.captionEdit.toPlainText()
        post = {"image": image, "caption": caption}
        self.parent.addPost(post)
        self.close()

class PostWidget(QWidget):
    def __init__(self, post):
        super().__init__()

        self.post = post

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.imageLabel = QLabel()
        self.layout.addWidget(self.imageLabel)

        image = QImage(self.post["image"])
        pixmap = QPixmap.fromImage(image)
        self.imageLabel.setPixmap(pixmap)

        self.captionLabel = QLabel(self.post["caption"])
        self.layout.addWidget(self.captionLabel)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    instagram = Instagram()
    sys.exit(app.exec_())
