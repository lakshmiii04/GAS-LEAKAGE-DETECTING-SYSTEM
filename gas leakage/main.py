from machine import Pin, ADC
import time

gas_sensor = ADC(26)        
led = Pin(14, Pin.OUT)      
buzzer = Pin(15, Pin.OUT)   

THRESHOLD = 30000          

print("Gas Leakage Detector Started")


while True:
    gas_value = gas_sensor.read_u16()   
    print("Gas Level:", gas_value)

    if gas_value > THRESHOLD:
        led.on()
        buzzer.on()
        print("⚠ GAS LEAKAGE DETECTED!")
    else:
        led.off()
        buzzer.off()
        print("Gas level normal")

    time.sleep(1)