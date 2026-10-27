import RPi.GPIO as GPIO
import time as time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)    


        self.last_dac_number = 0

    # 3. Деструктор
    def __del__(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    # 4. Метод подачи числа на вход ЦАП
    def number_to_dac(self, number):
        """
        Преобразует число в двоичный вид и подает на соответствующие пины.
        number - целое число от 0 до 255 (для 8-битного ЦАП).
        """
        number = max(0, min(255, int(number)))
        
        for i in range(8):
            bit_value = (number >> (7 - i)) & 1
            GPIO.output(self.bits_gpio[i], bit_value)
            
        self.last_dac_number = number

    def sequential_counting_adc(self):
        """
        Перебирает значения от 0 до 255, пока напряжение на ЦАП не превысит входное.
        Возвращает число, поданное на ЦАП последним.
        """
        for number in range(256): 
            self.number_to_dac(number)
            
           
            time.sleep(self.compare_time)
            
            
            comp_state = GPIO.input(self.comp_gpio)
            
            if self.verbose:
                print(f"Подано на ЦАП: {number}, Компаратор: {comp_state}")
            
            if comp_state == 1:
                return number
        
        
        return 255

    def get_sc_voltage(self):
        """
        Возвращает измеренное напряжение в Вольтах.
        """
        
        raw_value = self.sequential_counting_adc()
        voltage = (raw_value / 255.0) * self.dynamic_range
        
        if self.verbose:
            print(f"Сырое значение: {raw_value}, Напряжение: {voltage:.3f} В")
            
        return voltage


if __name__ == '__main__':
    
    DYNAMIC_RANGE = 3.3 
    
    adc = None
    try:
        
        adc = R2R_ADC(dynamic_range=DYNAMIC_RANGE, verbose=True)
        
        print("Начало измерений. ")
        

        while True:
            
            voltage = adc.get_sc_voltage()
   
            print(f"Измеренное напряжение: {voltage:.3f} В")
            print("-" * 30)
            time.sleep(1)    

    except KeyboardInterrupt:
        print("\nЛол")
    finally:
        if adc is not None:
            adc.__del__()
        print("Настройки GPIO очищены.")                                                         