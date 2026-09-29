import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac_bits = [16, 20, 21, 25, 26,17,27,22]
GPIO.setup(dac_bits, GPIO.OUT)
dynamic_range = 3.3

def voltage_to_number(voltadge):
    if not (0.0<= voltage<=dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B")
        print("Устанавливаем 0.0 В")
        return 0 
    return int(voltage/dynamic_range*255)

def dec2bin(number):
    return[int(element) for element in bin(number)[2:].zfill(8)]
    print(number)
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            dec2bin(number)
            print(number)
            print(dec2bin(number))
            bits = dec2bin(number)
            for i in range(8):
                GPIO.output(dac_bits[i],bits[i])
            
        
        except ValueError:
            print("Вы ввели не число.Попробуйте еще раз\n")
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()

