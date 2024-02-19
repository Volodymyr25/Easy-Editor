from PyQt5.QtCore import Qt    
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QListWidget,QLineEdit,QTextEdit,QVBoxLayout,QHBoxLayout,QInputDialog,QFileDialog
from PIL import Image 
from PIL import ImageFilter 
import os 

from PyQt5.QtGui import QPixmap

 
app = QApplication([]) 
 
main_win = QWidget() 
main_win.setWindowTitle("Photo editor") 
main_win.resize(800,600) 
 
btn_papka = QPushButton("Папка") 
btn_left = QPushButton("Ліво") 
btn_right = QPushButton("Право") 
btn_glass = QPushButton("Дзеркало") 
btn_blur = QPushButton("Блюр") 
btn_blackandwhite = QPushButton("ч/б") 
spusok = QListWidget() 
Tekst = QLabel("photo")
 
 
row4 = QHBoxLayout() 
row2 = QHBoxLayout() 
 
 
row3 = QVBoxLayout() 
row1 = QVBoxLayout() 
 
 
row2.addWidget(btn_left) 
row2.addWidget(btn_right) 
row2.addWidget(btn_glass) 
row2.addWidget(btn_blur) 
row2.addWidget(btn_blackandwhite) 
 
row1.addWidget(btn_papka) 
row1.addWidget(spusok) 
 
row3.addWidget(Tekst) 
row3.addLayout(row2) 
row4.addLayout(row1,20) 
row4.addLayout(row3,80) 
 
 
main_win.setLayout(row4) 
 
workdir = '' 
 
def chooseWorkdir(): 
    global workdir 
    workdir = QFileDialog.getExistingDirectory() 
 
 
def filter(files, extensions): 
    results = [] 
    for filename in files: 
        for ext in extensions: 
            if filename.endswith(ext): 
                results.append(filename) 
    return results 
 
 
def showFilenameList(): 
    global workdir 
    extensions = ['.jpg','.png','.gif','.jpeg'] 
    chooseWorkdir() 
    filenames = filter(os.listdir(workdir), extensions) 
    spusok.clear() 
    for filename in filenames: 
        spusok.addItem(filename) 
 

def file_save(self):
    path = os.path.join(self.dir, self.new_folder)
    if not os.path.isdir(path):
        os.mdir(path)
    image_path = os.path.join(path, self.filename)
    self.image.save(image_path)


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self,dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def showImage(self,path):
        Tekst.hide()
        pixmapimage = QPixmap(path)
        w, h = Tekst.width(), Tekst.height()
        pixmapimage = pixmapimage.scarled(w,h, Qt.KeepAspectRatio)
        Tekst.setPixmap(pixmapimage)
        Tekst.show()

    def do_bw(self):
        self.image=self.image.convert("L")
        self.image = self.image
        self.file_save()
        image_path = os.path.join(self.dir, self.new_folder, self.filename)
        self.showImage(image_path)

    def do_left(self):
        self.image=self.image.transpose(Image.ROTATE_270)
        self.file_save()
        image_path = os.path.join(self.dir, self.new_folder, self.filename)
        self.showImage(image_path)

    def do_right(self):
        self.image=self.image.transpose(Image.ROTATE_90)
        self.file_save()
        image_path = os.path.join(self.dir, self.new_folder, self.filename)
        self.showImage(image_path)

    def do_flip(self):
        self.image=self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.file_save()
        image_path = os.path.join(self.dir, self.new_folder, self.filename)
        self.showImage(image_path)

    def do_sharp(self):
        self.image=self.image.filter(ImageFilter.SHARPEN)
        self.file_save()
        image_path = os.path.join(self.dir, self.new_folder, self.filename)
        self.showImage(image_path)

workimage = ImageProcessor()
def showChosenImage():
    if spusok.currentRow() >= 0:
        filename = btn_papka.currentItem().text()
        workimage.loadImage(workdir,filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

spusok.currentRowChanged.connect(showChosenImage)

main_win.show()
app.exec_()
