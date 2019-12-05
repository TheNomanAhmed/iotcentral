# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

# Pi_3iq_python_sample/main.py

import datetime
import sys
import connection

sys.path.append('_1bs') # search in _1bs interface
import telemetryStateEvent__1bs as _1bs_telemetry
import deviceProperties__1bs as _1bs_property
import commands__1bs as _1bs_command

# want to connect another device? just update the credentials below
SCOPE_ID = ''
DEVICE_ID = ''
KEY = ''

gCounter = 0
gDevice = None

def callback(info): # iotc.IOTCallbackInfo
  global gDevice

  if gDevice == None:
    gDevice = info.getClient()

  if info.getEventName() == 'ConnectionStatus':
    if info.getStatusCode() == 0:
      if gDevice.isConnected():
        print(str(datetime.datetime.now()), 'Connected!')
        return
    print(str(datetime.datetime.now()), 'Connection Lost?')
    gDevice = None
    return

  if info.getEventName() == 'SettingsUpdated':
    print(str(datetime.datetime.now()), 'Received an update to device settings.')

    _1bs_property.Process(gDevice, info)

  if info.getEventName() == 'Command':
    print(str(datetime.datetime.now()), 'Received a C2D from cloud to device settings.')

    _1bs_command.Process(gDevice, info)

def main():
  global gCounter, gDevice

  while True:
    gDevice = connection.Connect(SCOPE_ID, DEVICE_ID, KEY, callback)

    while gDevice != None and gDevice.isConnected():
      gDevice.doNext() # do the async work needed to be done for MQTT
      if gCounter % 10 == 0: # every 10 seconds
        gCounter = 0

        # sending telemetry for _1bs interface
        print(str(datetime.datetime.now()), 'sending telemetry for _1bs interface')
        _1bs_telemetry.Send(gDevice)
        # sending property update for _1bs interface
        print(str(datetime.datetime.now()), 'sending property updates for _1bs interface')
        _1bs_property.Update(gDevice)

      gCounter += 1

main()
