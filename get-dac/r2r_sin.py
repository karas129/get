import r2r_dac as r2r
import signal_generator as sg
import time as time

amplitude = 3.2
signal_frequency  = 10
sampling_frequency = 1000
start_time = 0



if __name__== "__main__":
    try:
        dac = r2r.R2R_DAC(12,True)
        star_time = time.time()

        while True:
            current_time = time.time() -  start_time
            norm_value = sg.get_sin_wave_amplitude(signal_frequency,current_time)
            voltage = norm_value *amplitude
            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)
                 
    finally:
        dac.deinit()


