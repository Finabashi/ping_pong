from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

red = (255, 0, 0)

x = 3
y = 5
ysens = 1
xsens = 1




def dessine_ball():
  global x, y, xsens, ysens
  x = x + xsens
  y = y + ysens

  sense.set_pixel(x,y,red)

  if x == 0:
    xsens = 1
  if x == 7:
    xsens = -1

  if  y == 0:
    ysens = 1
  elif y == 7:
    ysens = -1


while True:
  sense.clear()
  dessine_ball()


  sleep(0.3)


