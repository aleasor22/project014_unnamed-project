import tkinter
from PIL import ImageTk, Image
from pynput import keyboard

#class INPUTS():
#	def __init__(self):
#		self.currPos = None
#		self.lastPos = None

class OBJECT():
	def __init__(self, canvasID):
		self.canvasID = canvasID

		self.bbox = None
		self.coords = None
		self.colorID = None
		self.imgID = None

class MY_TKINTER():
	def __init__(self, title:str, width:int=1280, height:int=768):
		self.root = tkinter.Tk()
		self.root.title(str(title))
		#root.iconbitmap('file-location')
		self.width = width
		self.height= height
		self.root.geometry(f"{width}x{height}")

		self.__bg_canvas = None
		self.__bg_tileMatrix = [[]]
		self.__bg_tiles = {}
		self.__fg_player = {}
		#self.inputs = INPUTS()

	def renderImages(self, name:str, fileLoc:str, pos_x:int, pos_y:int, rotate:int=0):
		imgPil = Image.open(str(fileLoc))
		newPil = imgPil.rotate(rotate, expand=True)
		
		imgTk = ImageTk.PhotoImage(newPil)
		canvasID = self.__bg_canvas.create_image(pos_x+33, pos_y+33, image=imgTk, anchor="center")



		self.__fg_player[str(name)] = OBJECT(canvasID)
		self.__fg_player[str(name)].imgID = imgTk
		self.__fg_player[str(name)].coords = (pos_x+33, pos_y+33)
		

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
				self.__bg_canvas.create_text((pos_x*64)+32, (pos_y*64)+32, text=f"{pos_x, pos_y}", fill="red")
				myID = f"{pos_x}|{pos_y}"
				self.__bg_tiles[myID] = OBJECT(canvasID=tmp)
				self.__bg_tiles[myID].bbox = myBbox
				self.__bg_tiles[myID].coords = (myBbox[0], myBbox[1])
				self.__bg_tiles[myID].colorID = color
				self.__bg_tileMatrix[pos_x].append(myBbox)

			self.__bg_tileMatrix.append([])
			if colorBool:
				colorBool = False
			else:
				colorBool = True
		
	
	#def printMatrix(self):
	#	for x in range(len(self.__bg_tileMatrix)):
	#		for y in range(len(self.__bg_tileMatrix[x])):
	#			print(self.__bg_tileMatrix[x][y], end=" ")
	#		print()
	
	def findMyTile(self, coords):
		for x in range(len(self.__bg_tileMatrix)):
			for y in range(len(self.__bg_tileMatrix[x])):
				currTile = self.__bg_tileMatrix[x][y]
				if currTile[0] < coords[0] and currTile[2] > coords[0]:
					if currTile[1] < coords[1] and currTile[3] > coords[1]:
						#print(f"({x}, {y})")
						return (x, y)

	def mousePosition(self, event):
		#print(f"Mouse Pos: {self.findMyTile((event.x, event.y))}")
		#print(f"Player Pos: {self.findMyTile(self.__fg_player["player"].coords)}")

		path = self.findPath(event)
		print(path)
		for index in range(len(path)):
			try:
				x, y = path[index][1]
				if path[index] == path[-1]: ##Happens with the last item of list is present
					print(f"{path[index]} vs {path[-1]}")
					if path[index][0] == "right":
						self.renderImages(f"line-{index}", "art/Path-vUPARROW.png", pos_x=x, pos_y=y, rotate=270)
					elif path[index][0] == "left":
						self.renderImages(f"line-{index}", "art/Path-vUPARROW.png", pos_x=x, pos_y=y, rotate=90)
					elif path[index][0] == "higher":
						self.renderImages(f"line-{index}", "art/Path-vUPARROW.png", pos_x=x, pos_y=y, rotate=0)
					elif path[index][0] == "lower":
						self.renderImages(f"line-{index}", "art/Path-vUPARROW.png", pos_x=x, pos_y=y, rotate=180)
				else:
					if path[index][0] == path[index+1][0]: ##When the lines are straight
						if path[index][0] == "right" or path[index][0] == "left":
							self.renderImages(f"line-{index}", "art/Path-vLINE.png", pos_x=x, pos_y=y, rotate=90)
						elif path[index][0] == "higher" or path[index][0] == "lower":
							self.renderImages(f"line-{index}", "art/Path-vLINE.png", pos_x=x, pos_y=y, rotate=0)

					if path[index][0] != path[index+1][0] and path[index][0] == "right":
						if path[index+1][0] == "lower":
							self.renderImages(f"line-{index}", "art/Path-vBEND.png", pos_x=x, pos_y=y, rotate=0)
						elif path[index+1][0] == "higher":
							self.renderImages(f"line-{index}", "art/Path-vBEND.png", pos_x=x, pos_y=y, rotate=270)
					elif path[index][0] != path[index+1][0] and path[index][0] == "left":
						if path[index+1][0] == "lower":
							self.renderImages(f"line-{index}", "art/Path-vBEND.png", pos_x=x, pos_y=y, rotate=90)
						elif path[index+1][0] == "higher":
							self.renderImages(f"line-{index}", "art/Path-vBEND.png", pos_x=x, pos_y=y, rotate=180)
					elif path[index][0] != path[index+1][0] and path[index][0] == "lower":
						if path[index+1][0] == "right":
							self.renderImages(f"line-{index}", "art/Path-vBEND.png", pos_x=x, pos_y=y, rotate=180)
						elif path[index+1][0] == "left":
							self.renderImages(f"line-{index}", "art/Path-vBEND.png", pos_x=x, pos_y=y, rotate=270)
					elif path[index][0] != path[index+1][0] and path[index][0] == "higher":
						if path[index+1][0] == "right":
							self.renderImages(f"line-{index}", "art/Path-vBEND.png", pos_x=x, pos_y=y, rotate=90)
						elif path[index+1][0] == "left":
							self.renderImages(f"line-{index}", "art/Path-vBEND.png", pos_x=x, pos_y=y, rotate=0)

			except IndexError as e:
				print(e)
				continue

	def findPath(self, event):
		mousePos = self.findMyTile((event.x, event.y))
		playerPos = self.findMyTile(self.__fg_player["player"].coords)
		targetPos = playerPos

		##Resets the fg_player dictionary to remove old lines when the mouse moves
		pathDir = []
		temp = {}
		for key in self.__fg_player.keys():
			if "line-" not in key:
				temp[key] = self.__fg_player[key]
		self.__fg_player = temp
		
		try:
			while mousePos != targetPos:
				if mousePos[0] < targetPos[0]:
					targetPos = (targetPos[0]-1, targetPos[1]) #Moves the target tile one to the left.

					x1, y1, x2, y2 = self.__bg_tileMatrix[targetPos[0]][targetPos[1]]
					pathDir.append(("left", (x1, y1)))
				elif mousePos[0] > targetPos[0]:
					targetPos = (targetPos[0]+1, targetPos[1]) #Moves the target tile one to the right.

					x1, y1, x2, y2 = self.__bg_tileMatrix[targetPos[0]][targetPos[1]]
					pathDir.append(("right", (x1, y1)))
				if mousePos[1] < targetPos[1]:
					targetPos = (targetPos[0], targetPos[1]-1) #Moves the target tile one to the higher.

					x1, y1, x2, y2 = self.__bg_tileMatrix[targetPos[0]][targetPos[1]]
					pathDir.append(("higher", (x1, y1)))
				elif mousePos[1] > targetPos[1]:
					targetPos = (targetPos[0], targetPos[1]+1) #Moves the target tile one to the lower.

					x1, y1, x2, y2 = self.__bg_tileMatrix[targetPos[0]][targetPos[1]]
					pathDir.append(("lower", (x1, y1)))
			
			x1, y1, x2, y2 = self.__bg_tileMatrix[mousePos[0]][mousePos[1]]
			pathDir.append((pathDir[-1][0], (x1, y1)))
			
		
		except TypeError as e:
			print(e)

		return pathDir

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
		x1, y1, x2, y2 = self.__bg_tiles["9|5"].bbox
		#print(map.get_tileInfo()["5|10"][0])
		self.renderImages("player", "art/tmp-player.png", x1, y1, rotate=90)

		self.__bg_canvas.bind("<Motion>", self.mousePosition)



game = MY_TKINTER("Demo Game [v0.0.13-ref001]")

game.game_start()
game.mainLoop()
