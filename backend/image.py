import tkinter
from PIL import ImageTk, Image

class IMAGE():
	def __init__(self, mapObj):
		self.__canvas = mapObj.get_canvas()
		self._allImageData = {}
		self._allImages	= {}
		pass


	def loadImage(self, name:str, fileLoc:str):
		##Loads Images, then Saves the base data to a dictionary
		imgPil = Image.open(str(fileLoc))
		self._allImageData[name] = ImageTk.PhotoImage(imgPil)

	def placeImage(self, name:str, pos_x:int, pos_y:int):
		self._allImages[name] = self.__canvas.create_image(pos_x+33, pos_y+33, tag="temp", image=self._allImageData[name], anchor="center")