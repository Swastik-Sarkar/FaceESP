from machine import Pin

GREEN_LED = 15
RED_LED = 16
BUZZER = 17
BUTTON_ON_OFF = 18

green_led = Pin(GREEN_LED, Pin.OUT)
red_led = Pin(RED_LED, Pin.OUT)
buzzer = Pin(BUZZER, Pin.OUT)

def setup_hardware():
    green_led.off()
    red_led.off()
    buzzer.off()

def recognize_face():
    green_led.on()
    time.sleep(1)
    green_led.off()
