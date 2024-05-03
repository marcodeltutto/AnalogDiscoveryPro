## API for Digilent Analog Discover Pro

- `main.py` is the main API
- `adpro.py` is the digitizer class
- `WF_SDK` contains Digilent's helper functions to interact with the digitizer

### Instructions

- From the PrM server, log in to the digitizer via `ssh -L 8000:localhost:8000 digilent@10.226.35.155`
- Clone this repo, if not done already
- Enter and run the API: `sudo /home/digilent/.local/bin/uvicorn main:app --reload`

On the PrM server, you can control the digitizer via:
- `localhost:8000/lamp_control/on`: turns the flash lamp on
- `localhost:8000/lamp_control/off`: turns the flash lamp off
- `localhost:8000/lamp_frequency/10`: sets the lamp frequency to 10 Hz
- `localhost:8000/digitizer/start_capture`: starts the data acquisition
- `localhost:8000/digitizer/check_capture`: checks if the acquisition if over
- `localhost:8000/digitizer/get_data`: returns the collected data
- For more commands, see `main.py`. 

### Run Manually

- From the PrM server, log in to the digitizer via `ssh -L 8000:localhost:8000 digilent@10.226.35.155`
- Clone this repo, if not done already
- Run `python`, then:

```python
from adpro import ADPro

# Instantiate the digitizer class
digitizer = ADPro()

# Turn on the flash lamp (uses the waveform generator)
digitizer.lamp_on()

# Start a digitizer data acquisitio
digitizer.start_capture()

# Check for the acquisition to be completed
while not digitizer.check_capture():
    time.sleep(1)

# Turn off the flash lamp
digitizer.lamp_off()

# Retrieve the digitizer data
data = digitizer.get_data()
print(data)

# Close the digitizer
digitizer.close()
```

Check: [Getting Started with the WaveForms SDK](https://digilent.com/reference/test-and-measurement/guides/waveforms-sdk-getting-started) for more details.

