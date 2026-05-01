import tkinter
from PIL import ImageTk, Image

class IMAGE():
	def __init__(self, mapObj):
		self.__canvas = mapObj.get_canvas()
		self._allImageData = []

	def loadImage(self, fileLoc:str):
		##Loads Images, then Saves the base data to a dictionary
		imgPil = Image.open(str(fileLoc))
		tmp = ImageTk.PhotoImage(imgPil)
		self._allImageData.append(tmp)
		return tmp

	def placeImage(self, pilImg, pos_x:int, pos_y:int):
		##Returns the Canvas ID for the newly created Image
		print(pilImg, "test")
		return self.__canvas.create_image(pos_x+33, pos_y+33, image=pilImg, anchor="center")
