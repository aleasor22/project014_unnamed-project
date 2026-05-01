import tkinter

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
		print(self.width, self.height)
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

				tmp = self.__bg_canvas.create_rectangle(pos_x*64, pos_y*64, (pos_x*64)+64, (pos_y*64)+64, fill=color)
				self.__bg_tiles[f"{pos_x}|{pos_y}"] = [(pos_x*64, pos_y*64, (pos_x*64)+64, (pos_y*64)+64), tmp, color]


			if colorBool:
				colorBool = False
			else:
				colorBool = True
		pass

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