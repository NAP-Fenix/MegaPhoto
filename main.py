from PyQt5 import QtCore, QtGui, QtWidgets #pip install PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
from PIL import Image , ImageFont , ImageFilter , ImageDraw , ImageEnhance


app = QtWidgets.QApplication([])
MainWindow = QWidget()
MainWindow.resize(900,700)
MainWindow.setWindowTitle('MagicPhotos')
folder = QPushButton('Папочка')
list_photos = QListWidget()
image = QLabel('foto not faund')
effect_left = QPushButton('Поворот на лево')
effect_right = QPushButton('Поворот на право')
effect_mirror = QPushButton('Отзеркалить')
effect_Sharpness = QPushButton('Резкость')
effect_black = QPushButton('Чёрно-Белый')

MainVertical = QHBoxLayout()

FloderVer = QVBoxLayout()
FloderVer.addWidget(folder,alignment = Qt.AlignLeft)
FloderVer.addWidget(list_photos,alignment = Qt.AlignLeft)
ImageVer = QVBoxLayout()
ImageVer.addWidget(image, 65)
ButtonsVer = QHBoxLayout()
ButtonsVer.addWidget(effect_left)
ButtonsVer.addWidget(effect_right)
ButtonsVer.addWidget(effect_mirror)
ButtonsVer.addWidget(effect_Sharpness)
ButtonsVer.addWidget(effect_black)

ImageVer.addLayout(ButtonsVer)
MainVertical.addLayout(FloderVer , 20)
MainVertical.addLayout(ImageVer , 80)

MainWindow.setLayout(MainVertical)

class ImageProcessor():
	def __init__(self):
		self.filename = None
		self.original = None
		self.pics = ("nev/")

	def loadImage(self,filename):
		self.filename = filename
		paf = os.path.join(dirlist,self.filename)
		try:
		    self.original = Image.open(paf)
		except:
		    print('Файл не найден!')
	def showimage (self,path):
		image.hide()
		paixpapimage = QPixmap(path)
		w, h =  image.width(), image.height()
		paixpapimage = paixpapimage.scaled (w, h, Qt.KeepAspectRatio)
		image.setPixmap(paixpapimage)
		image.show()
	def saveimage(self):
		path=os.path.join(dirlist,self.pics)
		if not(os.path.exists(path) or os.path.isdir(path)):
			os.mkdir(path)
		fullpath = os.path.join(path, self.filename)
		self.original.save(fullpath)
		

	def black(self):
		self.original = self.original.convert('L')
		self.saveimage()
		fullpath = os.path.join(dirlist, self.pics, self.filename)
		self.showimage(fullpath)	


dirlist = ''
def chooseWorkdir():     
	global dirlist                                            
	dirlist = QFileDialog.getExistingDirectory()

def filter(name,exe):
	result = list()
	for filename in name:
		for extension in exe:
			if filename.endswith(extension):
				result.append(filename)
	return result

def showFilenamesList():
	chooseWorkdir()
	ext = ['jpg','bmp','jpeg','png','gaif']
	keep = filter(os.listdir(dirlist),ext)
	list_photos.clear()
	list_photos.addItems(keep)


def showChocenImage():
	if list_photos.currentRow() >= 0:
		filename = list_photos.currentItem().text()
		workimage.loadImage(filename)
		image_path = os.path.join(dirlist,workimage.filename)
		workimage.showimage(image_path)
	
workimage = ImageProcessor()

folder.clicked.connect(showFilenamesList)
effect_black.clicked.connect(workimage.black)
list_photos.currentRowChanged.connect(showChocenImage)


MainWindow.show()
app.exec_()








































