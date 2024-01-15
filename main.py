# main.py

import time

from fastapi import FastAPI
from adpro import ADPro

app = FastAPI()

_digitizer = ADPro()

@app.get("/")
async def root():
    # mc.count()
    return {"message": "Hello World"}


@app.get("/lamp_control/{status}")
async def lamp_control(status):
    s = status.lower() in ['on', 'true', '1', 't', 'y', 'yes']
    if s:
        print('Turn lamp on')
        _digitizer.lamp_on()
    else:
        print('Turn lamp off')
        _digitizer.lamp_off()
    return {"status": status}

@app.get("/lamp_frequency/{freq}")
async def frequency(freq):
    print('Setting frequency to', float(freq))
    _digitizer.set_lamp_frequency(float(freq))
    return {"frequency": freq}

@app.get("/digitizer/{command}")
async def digitizer(command):

    if command == 'start_capture':
        print('start_capture')
        status = _digitizer.start_capture()
        return {"status": status}

    elif command == 'check_capture':
        print('check_capture')
        status = _digitizer.check_capture()
        return {"status": status}

    elif command == 'get_data':
        print('get_data')
        data = _digitizer.get_data()
        return {"data": data}

    elif command == 'busy':
        busy = _digitizer.busy()
        return {"busy": busy}

    elif command == 'trigger_sample':
        return {"trigger_sample": _digitizer.get_trigger_sample()}

    elif command == 'samples_per_second':
        return {"samples_per_second": _digitizer.get_samples_per_second()}

    elif command == 'set_samples_per_second':
        return {"set_samples_per_second": None}

    elif command == 'number_acquisitions':
        return {"number_acquisitions": _digitizer.get_number_acquisitions()}

    elif command == 'set_number_acquisitions':
        return {"set_number_acquisitions": None}

    elif command == 'pre_trigger_samples':
        return {"pre_trigger_samples": _digitizer.get_pre_trigger_samples()}

    elif command == 'post_trigger_samples':
        return {"post_trigger_samples": _digitizer.get_post_trigger_samples()}

    elif command == 'input_range_volts':
        return {"input_range_volts": _digitizer.get_input_range_volts()}


    return {"command": command}


if __name__ == "__main__":

    print('About to call lamp_on')
    _digitizer.lamp_on()
    print('Called lamp_on')
    time.sleep(2)
    print('About to call lamp_off')
    _digitizer.lamp_off()
    print('Called lamp_off')

    _digitizer.close()
