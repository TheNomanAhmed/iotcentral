# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

# Pi_3iq_python_sample/@_1bs/deviceProperties__1bs.py

import json
import datetime

def createBlob():
  return {
    'state': 16, # <- try another value!
  }

def Update(device):
  device.sendProperty(json.dumps(createBlob()))

def Process(device, info):
  value = info.getPayload()
  key = info.getTag()

  if key == 'name':
    print(str(datetime.datetime.now()), 'name is updated to', value, '')
    return

  if key == 'brightness':
    print(str(datetime.datetime.now()), 'brightness is updated to', value, '')
    return

  print(str(datetime.datetime.now()),
        'WARNING!: unknown property', key, 'with value', value, 'is received.')
