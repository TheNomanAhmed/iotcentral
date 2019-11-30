# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

# Pi_3iq_python_sample/@_1bs/commands__1bs.py

import datetime
from sense_hat import SenseHat
sense = SenseHat()


r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]

image = [
r,r,r,r,r,r,r,r,
e,e,e,r,r,e,e,e,
e,r,r,o,o,r,r,e,
r,o,o,y,y,o,o,r,
o,y,y,g,g,y,y,o,
y,g,g,b,b,g,g,y,
b,b,b,i,i,b,b,b,
b,i,i,v,v,i,i,b
]

sense.clear()



def Process(gDevice, info):

  if info.getTag() == 'turnon':
    sense.set_pixels(image)
    print(str(datetime.datetime.now()),
          '"turnon" C2D is received with payload', info.getPayload())

  if info.getTag() == 'turnoff':
    sense.clear()
    print(str(datetime.datetime.now()),
          '"turnoff" C2D is received with payload', info.getPayload())

  if info.getTag() == 'DisplayText':
    p = info.getPayload()
    sense.show_message(p)
    print(str(datetime.datetime.now()),
          '"DisplayText" C2D is received with payload', info.getPayload())

  if info.getTag() == 'BooleanCommand':
    print(str(datetime.datetime.now()),'"BooleanCommand" C2D is received with payload', info.getPayload())
