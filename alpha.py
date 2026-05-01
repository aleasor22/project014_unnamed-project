from backend import *


map = CANVAS("Demo Game [v0.0.11-ref001]")

map.loadingMaps()

render = IMAGE(map)
input = INPUTS(map)


##Places Images to screen
x1, y1, x2, y2 = map.get_tileInfo()["5|10"].bbox
#print(map.get_tileInfo()["5|10"][0])
render.placeImage(render.loadImage("art/tmp-player.png"), x1, y1)


map.mainLoop()
