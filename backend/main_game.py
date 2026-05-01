import tkinter

class CANVAS_OBJECT():
	def __init__(self, bbox, canvasID, colorID):
		self.bbox = bbox
		self.canvasID = canvasID
		self.colorID = colorID

class CANVAS():
	def __init__(self, title:str, width:int=1280, height:int=768):
		self.root = tkinter.Tk()
		self.root.title(str(title))
		self.width = width
		self.height= height
		self.root.geometry(f"{width}x{height}")

		self.__bg_canvas = None
		self.__bg_tiles = {}
		#root.iconbitmap('file-location')

	def loadingMaps(self):
		## Where canvas objests get rendered
		# Eventually can take in CSV files with pre-determined mapes
		#print(self.width, self.height)
		self.__bg_canvas = tkinter.Canvas(self.root, width=self.width, height=self.height, bg="gray")
		self.__bg_canvas.pack()

		colorBool = False
		for pos_x in range(int(self.width/64)):
			for pos_y in range(int(self.height/64)):
				#print(f"({pos_x*64}, {pos_y*64})")
				if colorBool:
					color = "#404040"
					colorBool = False
				else:
					color = "#C0C0C0"
					colorBool = True

				myBbox = (pos_x*64, pos_y*64, (pos_x*64)+64, (pos_y*64)+64)
				tmp = self.__bg_canvas.create_rectangle(myBbox, fill=color)
				self.__bg_tiles[f"{pos_x}|{pos_y}"] = CANVAS_OBJECT(bbox=myBbox, canvasID=tmp, colorID=color)


			if colorBool:
				colorBool = False
			else:
				colorBool = True
		
	def findMyTile(self, coords):
		for key, value in self.__bg_tiles.items():
			#print(keys, values)
			if value.bbox[0] < coords[0] and value.bbox[2] > coords[0]:
				if value.bbox[1] < coords[1] and value.bbox[3] > coords[1]:
					print(f"Within box: {key}") 
					return key

	def mainLoop(self):
		##Main Code Block:
		# Anything that needs to be continuously called
		#
		#
		#
		#
		## END OF BLOCK

		self.root.mainloop()

	def get_tileInfo(self):
		return self.__bg_tiles

	def get_canvas(self):
		return self.__bg_canvas