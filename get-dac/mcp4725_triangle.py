import mcp4725_driver 
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
start_time = 0

if __name__== "__main__":
    try:
        dac = mcp4725_driver.MCP4725(dynamic_range=3.3, address=0x61, verbose=True)
        start_time = time.time()

        while True:
            current_time = time.time() - start_time  
            # тут добавил
            norm_value = sg.get_triangle_wave_amplitude(signal_frequency, current_time)
            
            voltage = norm_value * amplitude
            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)       
    except KeyboardInterrupt:
        print("Остановлено")
    finally:
        if 'dac' in locals():
            dac.deinit()
