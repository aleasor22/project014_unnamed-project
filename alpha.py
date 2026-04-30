from backend import *


map = CANVAS("Demo Game [v0.0.1]")
render = IMAGE(map.root)

map.loadingMaps()

map.mainLoop()
