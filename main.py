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
        # return {"data": [1, 2, 3, 4, 5]*1000}
        # return {"command": command}
    elif command == 'busy':
        print('busy')
    # elif command == 'get_data':
    #     print('get_data')
    # elif command == 'get_data':
    #     print('get_data')

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
