from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from random import randint

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
myrectangle = RectangleAsset(50, 50, thinline, green)
mysprites = [Sprite(myrectangle, (x*randint(-10,10), x*randint(-10,10))) for x in range(50)]
#mysprite = Sprite(myrectangle, (300, 300))

def step():
  for s in mysprites:
      s.x += randint(-5,5)
      s.y += randint(-5,5)

myapp = App()
myapp.run(step)
