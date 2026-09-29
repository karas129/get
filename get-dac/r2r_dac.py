import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
gpio_bits = [16, 20, 21, 25, 26,17,27,22]
GPIO.setup(gpio_bits, GPIO.OUT)
dynamic_range = 3.3

class R2R_DAC:
    def __init__(self,gpio_bits,dynamic_range,verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.setup(self.gpio_bits,0)
        GPIO.cleanup()
    
    def set_number(self, number):
        bits = [int(element) for element in bin(number)[2:].zfill(8)]
        for i in range(8):
            GPIO.output(gpio_bits[i],bits[i])
        if self.verbose:
            print(f"Установлено число: {number}")
    
    def set_voltage(self,voltage):
        if not (0.0<= voltage<=dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B")
            print("Устанавливаем 0.0 В")
            self.set_number(0)
            return
        number = int(voltage/self.dynamic_range*255)
        bits = [int(element) for element in bin(number)[2:].zfill(8)]
        self.set_number(number)
        if self.verbose:
            print(f"Установлено напряжение: {voltage}В (число:{number})")
            print(bits)
if __name__== "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26,17,27,22],3.183,True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели  не число")
    finally:
        dac.deinit()



            
