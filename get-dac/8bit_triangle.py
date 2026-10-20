import time
from r2r_dac import R2R_DAC  


AMPLITUDE = 2.0       
FREQUENCY = 50.0      
SAMPLE_RATE = 1000    


dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, False)

def generate_triangle():
    print(f"Генерация: Амплитуда={AMPLITUDE}В, Частота={FREQUENCY}Гц, Fs={SAMPLE_RATE}Гц")
   
    
    
    period = 1.0 / FREQUENCY
    
    dt = 1.0 / SAMPLE_RATE
    
    start_time = time.perf_counter() 
    try:
        while True:
            
            current_time = time.perf_counter() - start_time
            
            
            phase = (current_time % period) / period
            
            
            if phase < 0.5:
                voltage = (phase * 2) * AMPLITUDE
            else:
                voltage = (2 - phase * 2) * AMPLITUDE
            
            
            dac.set_voltage(voltage)
            
            
            time.sleep(dt)
            
    except KeyboardInterrupt:
        print("\nГенерация остановлена.")
    finally:
        
        dac.set_voltage(0)
        dac.deinit()
        print("ЦАП деинициализирован.")

if __name__ == "__main__":
    generate_triangle()