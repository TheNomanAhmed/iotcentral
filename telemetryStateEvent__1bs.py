# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

# Pi_3iq_python_sample/@_1bs/telemetryEventState.py

import json
from sense_hat import SenseHat
sense = SenseHat()
def CreateBlob():
  return {
    'temp': str(sense.get_temperature()), # <- try another value!
    'humid': str(sense.get_humidity()), # <- try another value!
    'pressure': str(sense.get_pressure()), # <- try another value!
  }

def Send(device):
  device.sendTelemetry(json.dumps(CreateBlob()))
