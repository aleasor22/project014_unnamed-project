from backend import *


map = CANVAS("Demo Game [v0.0.11]")

map.loadingMaps()

render = IMAGE(map)

##Creates Image Objects
render.loadImage("Player", "art/tmp-player.png")
render.loadImage("tmp-arrow", "art/Path-vUPARROW.png")
render.loadImage("tmp-line", "art/Path-vLINE.png")

##Places Images to screen
x1, y1, x2, y2 = map.get_tileInfo()["5|10"][0]
#print(map.get_tileInfo()["5|10"][0])
render.placeImage("Player", x1, y1)


map.mainLoop()
