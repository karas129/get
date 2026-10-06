import RPi.GPIO as GPIO
import smbus


class MCP4725:
    def __init__(self,dynamic_range,address = 0x61,verbose = True  ):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()
    
    def set_number(self,number):
        if not isinstance(number,int):
            print('чувак ток целые числа')
        if not (0<=number<=4095):
            print('число выходит за рязрядность MCP4752(12 БИТ')

        first_byte = self.wm|self.pds|number>>8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte,second_byte)

        if self.verbose:
            print(f"Число: {number},отправленные по I2C данные:[0x{(self.address<<1):02X},0x{first_byte:02X}, 0x{second_byte:02x}]\n")
    def set_voltage(self,voltage):
        if voltage <0:
            voltage  = 0
        if voltage > self.dynamic_range:
            voltage = self.dynamic_range

        number = int((voltage/self.dynamic_range)*4095)
        self.set_number(number)
        

if __name__== "__main__":
    try:
        dac = MCP4725(dynamic_range = 5.11)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели  не число")
    finally:
        dac.deinit()
     