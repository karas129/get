import time
from r2r_adc import R2R_ADC 
from adc_plot import plot_voltage_vs_time


DYNAMIC_RANGE = 3.3 

def main():
   
    voltage_values = [] 
    time_values = []    
    duration = 3.0  
    adc = None
    
    try:
        adc = R2R_ADC(dynamic_range=DYNAMIC_RANGE, compare_time=0.0001)
        start_time = time.time()
        
        print(f"Начало измерений на {duration} секунд...")
 
        while (time.time() - start_time) < duration:
   
   
            voltage = adc.get_sc_voltage()
            voltage_values.append(voltage)
            
            current_time = time.time() - start_time
            time_values.append(current_time)
            
    except KeyboardInterrupt:
        print("\n лолололололо")
        
    finally:
        
        if adc is not None:
            
            del adc 
            
        if len(time_values) > 0:
            
            plot_voltage_vs_time(time_values, voltage_values, DYNAMIC_RANGE)
        else:
            print("Нет данных для построения графика.")

if __name__ == "__main__":
    main()