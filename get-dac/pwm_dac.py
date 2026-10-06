import RPi.GPIO as GPIO


class PWM_DAC:
    def __init__(self,gpio_pin,pwm_frequency,dynamic_range,verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
        self.pwm = GPIO.PWM(self.gpio_pin,pwm_frequency)

    def deinit(self):
        GPIO.setup(self.gpio_pin,0)
        GPIO.cleanup()
    
    def set_voltage(self,voltage):
        duty_cycle = (voltage/self.dynamic_range)*100.0
        self.pwm.ChangeDutyCycle(duty_cycle)
        if self.verbose:
            print('кэф заполнения =',duty_cycle)



if __name__== "__main__":
    try:
        dac = PWM_DAC(12,500,3.290,True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели  не число")
    finally:
        dac.deinit()
