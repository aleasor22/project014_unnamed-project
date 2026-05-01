import tkinter
from PIL import ImageTk, Image
from pynput import keyboard

class OBJECT():
	def __init__(self, canvasID):
		self.canvasID = canvasID

		self.bbox = None
		self.colorID = None
		self.imgID = None

class MY_TKINTER():
	def __init__(self, title:str, width:int=1280, height:int=768):
		self.root = tkinter.Tk()
		self.root.title(str(title))
		self.width = width
		self.height= height
		self.root.geometry(f"{width}x{height}")

		self.__bg_canvas = None
		self.__bg_tiles = {}
		self.__fg_player = {}
		#root.iconbitmap('file-location')

	def renderImages(self, name:str, fileLoc:str, pos_x:int, pos_y:int):
		imgPil = Image.open(str(fileLoc))
		tempVar = ImageTk.PhotoImage(imgPil)
		canvasID = self.__bg_canvas.create_image(pos_x+33, pos_y+33, image=tempVar, anchor="center")
		self.__fg_player[str(name)] = OBJECT(canvasID)
		self.__fg_player[str(name)].imgID = tempVar
		self.__fg_player[str(name)].bbox = imgPil.size
		

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
				myID = f"{pos_x}|{pos_y}"
				self.__bg_tiles[myID] = OBJECT(canvasID=tmp)
				self.__bg_tiles[myID].bbox = myBbox
				self.__bg_tiles[myID].colorID = color


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
	
	def game_start(self):
		
		self.loadingMaps()

		##Places Images to screen
		x1, y1, x2, y2 = self.__bg_tiles["5|10"].bbox
		#print(map.get_tileInfo()["5|10"][0])
		self.renderImages("player", "art/tmp-player.png", x1, y1)



game = MY_TKINTER("Demo Game [v0.0.12-ref001]")

game.game_start()
game.mainLoop()
