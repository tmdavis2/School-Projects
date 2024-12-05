import machine
import utime


right_sensor_pin = machine.ADC(26)  
center_sensor_pin = machine.ADC(27)  
left_sensor_pin = machine.ADC(28)


left_motor_forward = machine.Pin(20, machine.Pin.OUT)
left_motor_backward = machine.Pin(19, machine.Pin.OUT)
right_motor_forward = machine.Pin(6, machine.Pin.OUT)
right_motor_backward = machine.Pin(7, machine.Pin.OUT)


left_motor_pwm = machine.PWM(left_motor_forward)
right_motor_pwm = machine.PWM(right_motor_forward)

left_back_motor_pwm = machine.PWM(left_motor_backward)
right_back_motor_pwm = machine.PWM(right_motor_backward)


left_motor_pwm.freq(110)
right_motor_pwm.freq(110)

left_back_motor_pwm.freq(110)
right_back_motor_pwm.freq(110)


button_pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)


def set_motor_speed(left_speed, right_speed):
    left_motor_pwm.duty_u16(left_speed)
    right_motor_pwm.duty_u16(right_speed)
    
def set_back_motor_speed(back_left_speed, back_right_speed):
    left_back_motor_pwm.duty_u16(back_left_speed)
    right_back_motor_pwm.duty_u16(back_right_speed)

def read_sensor(sensor):
    return sensor.read_u16()

def move_forward():
    set_motor_speed(30000, 30000)  
    set_back_motor_speed(15000, 15000)


def turn_left():
    set_motor_speed(0, 20000)  
    set_back_motor_speed(12000, 5000)


def turn_right():
    set_motor_speed(20000, 0)  
    set_back_motor_speed(5000, 12000)


def stop():
    set_motor_speed(0,0)
    set_back_motor_speed(0,0)
    
    
button_toggle = False

while True:
    left_val = read_sensor(left_sensor_pin)
    center_val = read_sensor(center_sensor_pin)
    right_val = read_sensor(right_sensor_pin)
    
    print("Center:", center_val, " Left:", left_val, " Right:", right_val)
    
    if button_pin.value() == 1 and button_toggle == False:
        print("toggle on")
        button_toggle = True
    elif button_pin.value() == 1 and button_toggle == True:
        print("toggle off")
        button_toggle = False
    
    if button_toggle:
        if left_val > (center_val + 2000) and left_val > (right_val + 2000):
            turn_left()
        elif right_val > (center_val + 2000) and right_val > (left_val + 2000):
            turn_right()
        else:
            move_forward()
    else:
        stop()
    
    utime.sleep(0.01)  
