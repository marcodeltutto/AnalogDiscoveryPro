import time

from WF_SDK import device, scope, wavegen, tools, error

class ADPro():

    counter = 0

    _device_data = None
    _buffer = None
    _lamp_frequency = 1 # Hz
    _is_flashing = False

    _sampling_frequency = 2e6
    _buffer_size = 6000
    _amplitude_range = 100e-3
    _n_acquisitions = 10

    def __init__(self):
        print('myclass __init__')
        self._device_data = device.open()
        self.configure()

    def lamp_on(self):
        print('Turning lamp on')
        wavegen.generate(self._device_data,
                         channel=1,
                         function=wavegen.function.square,
                         offset=1,
                         frequency=self._lamp_frequency,
                         amplitude=1,
                         run_time=120)
        self._is_flashing = True

    def lamp_off(self):
        print('Turning lamp off')
        wavegen.close(self._device_data)

    def set_lamp_frequency(self, frequency):
        self._lamp_frequency = frequency # Hz
        if self._is_flashing:
            self.lamp_off()
            self.lamp_on()

    def configure(self):
        scope.open(self._device_data,
                   sampling_frequency=self._sampling_frequency,
                   buffer_size=self._buffer_size,
                   amplitude_range=self._amplitude_range,
                   n_acquisitions=self._n_acquisitions)
        scope.trigger(self._device_data, enable=True, source=scope.trigger_source.external[1], edge_rising=False)

    def start_capture(self):
        # self._buffer = scope.record(device_data, channel=1)
        return scope.start_capture(self._device_data)

    def check_capture(self):
        return scope.check_capture(self._device_data)

    def get_data(self):
        self._buffer = scope.get_data(self._device_data, [1, 2, 3, 4])
        return self._buffer

    def close(self):
        device.close(self._device_data)

    def busy(self):
        '''Not available for this digitizer'''
        return False

    def get_trigger_sample(self):
        return scope.data.trigger_pos

    def get_pre_trigger_samples(self):
        return scope.data.trigger_pos

    def get_post_trigger_samples(self):
        return 0

    def get_samples_per_second(self):
        return self._sampling_frequency

    def get_number_acquisitions(self):
        return self._n_acquisitions

    def set_number_acquisitions(self):
        pass

    def get_input_range_volts(self):
        return self.amplitude_range

    def print_f(self):
        print('Hi! print_f')

    def count(self):
        self.counter += 1
        print('counter', self.counter)


if __name__ == "__main__":
    digitizer = ADPro()

    print('About to call lamp_on')
    digitizer.lamp_on()
    print('Called lamp_on')
    time.sleep(10)
    print('About to call lamp_off')
    digitizer.lamp_off()
    print('Called lamp_off')

    digitizer.start_capture()
    while not digitizer.check_capture():
        time.sleep(1)
    print(digitizer.get_data())
    
    digitizer.close()
