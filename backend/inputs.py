from pynput import keyboard
from .image import *
import tkinter

class INPUTS():
	def __init__(self, mapObj):
		self.__mapObj = mapObj
		self.__canvas = mapObj.get_canvas()

		self.__canvas.bind("<Motion>", self.mousePosition)
		self._currMousePos = None
		self._lastMousePos = None
		self._currObject = None
		self._createObj = True
		
		self._render = IMAGE(mapObj)
		

	def mousePosition(self, event):
		#print(event.x, event.y)
		self._currMousePos = self.__mapObj.findMyTile((event.x, event.y))
		if self._currMousePos != None and self._currMousePos == self._lastMousePos:
			x1, y1, x2, y2 = self.__mapObj.get_tileInfo()[self._currMousePos].bbox
			if self._createObj:
				self._currObject = self._render.placeImage(self._render.loadImage("art/Path-vUPARROW.png"), x1, y1)
				print(f"CanvasID={self._currObject}")
			
			self._lastMousePos = self._currMousePos
			self._createObj = False
		else:
			print("THEY ARE DIFFERENT")
			self._createObj = True
			self.__canvas.delete(self._currObject)
			self._lastMousePos = self._currMousePos