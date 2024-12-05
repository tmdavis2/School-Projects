from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time
import random


# Init I2C using pins GP14 & GP15
i2c = I2C(1, scl = Pin(15), sda = Pin(14), freq = 400000)

#initializing the pins 
up = Pin(2, Pin.IN, Pin.PULL_UP)
down = Pin(3, Pin.IN, Pin.PULL_UP)
left = Pin(4, Pin.IN, Pin.PULL_UP)
right = Pin(5, Pin.IN, Pin.PULL_UP)
button1 = Pin(6, Pin.IN, Pin.PULL_UP)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)

# Initialize oled display
WIDTH  = 128 
HEIGHT = 64  
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

#ball starting position
ball_x = 64
ball_y = 5

#ball vertical and horizontal speed
#the x is randomaized to make the game a bit more challenging and to ensure the ball wont get stuck against the wall
ball_x_speed = random.randint(0, 4)
ball_y_speed = 4

#ball size
ball_width = 4
ball_height = 4

#starting point of the bar
bar_x = 64
bar_y = 60

#this should not need an explanation...
bar_x_speed = 5

#textures for ball and bar
#can be implemented and changed but the bar is just defined as a rectangle in the loops
bar = bytearray([ 0b11111111,
                  0b11111111,
                  0b11111111])

ball = bytearray([ 0b01110,
                   0b11111,
                   0b11111,
                   0b11111,
                   0b01110])

# Load the ball into a framebuffer 
fball = framebuf.FrameBuffer(ball, 5, 5, framebuf.MONO_HLSB)

#same for bar
fbar = framebuf.FrameBuffer(bar, 8, 3, framebuf.MONO_HLSB)


#1st game mode
#Classic pong
def game_mode_1():
    global ball_x, ball_y, ball_x_speed, ball_y_speed, Score, run, bar_x

    # Reset variables for the game mode
    ball_x = 64
    ball_y = 5
    ball_x_speed = random.randint(1, 4)
    ball_y_speed = 4
    bar_x = 64
    Score = 0
    run = True
    
    oled.fill(0)
    oled.blit(fball, ball_x, ball_y)
    oled.fill_rect(bar_x, bar_y, 20, 2, 1)
    oled.show()
    time.sleep(1)
    while run:
         
        
        oled.fill(0)
        
        oled.blit(fball, ball_x, ball_y)
        oled.fill_rect(bar_x, bar_y, 20, 2, 1)
        oled.show()
        
        ball_x += ball_x_speed
        ball_y += ball_y_speed
        
        if right.value() == 0:
            # right button pressed
            bar_x += bar_x_speed
            if bar_x + 20 > WIDTH:
                bar_x = WIDTH - 20
        elif left.value() == 0:
            # left button pressed
            bar_x -= bar_x_speed
            if bar_x < 0:
                bar_x = 0
        
        if ball_x <= 0 or ball_x >= WIDTH - 5:  
            ball_x_speed = -ball_x_speed
        if ball_y <= 0:
            ball_y_speed = -ball_y_speed
        if ball_y >= HEIGHT - 5:
    #         ball_y_speed = -ball_y_speed
            run = False
        
        if(ball_y + ball_height >= bar_y and (ball_x - bar_x) >= 0 and (ball_x - bar_x) <= 20):
            ball_y_speed = -ball_y_speed
            if ball_x_speed < 0:
                ball_x_speed = random.randint(-4, -1)
            else:
                ball_x_speed = random.randint(1, 4)
            Score += 1
        
        
        time.sleep(.05)



    oled.fill(0)
    oled.text("Game Over", 32, 32)
    oled.text(f"Score: {Score}", 32, 50)
    oled.show()
    time.sleep(5)
    
    
#2nd game mode
#there is a bar on the top and bottom that both move parallel when you press left or right on the dpad
#your aim is to prevent the ball from touching the top or bottom of the screen
def caged():
    global ball_x, ball_y, ball_x_speed, ball_y_speed, Score, run, bar_x, top_bar_x

    # Reset variables for the game mode
    ball_x = 64
    ball_y = 32  # Start ball in the middle of the screen
    ball_x_speed = random.randint(1, 4)
    ball_y_speed = 4
    bar_x = 64
    top_bar_x = 64  # Initial position for the top bar
    bar_width = 20
    bar_height = 2
    Score = 0
    run = True
    
    
    
    oled.fill(0)
    oled.blit(fball, ball_x, ball_y)
    oled.fill_rect(bar_x, bar_y, bar_width, bar_height, 1)
    oled.fill_rect(top_bar_x, 5, bar_width, bar_height, 1)
    oled.show()
    time.sleep(1)

    while run:
        oled.fill(0)

        # Draw the ball
        oled.blit(fball, ball_x, ball_y)

        # Draw the bottom bar
        oled.fill_rect(bar_x, bar_y, bar_width, bar_height, 1)

        # Draw the top bar
        oled.fill_rect(top_bar_x, 1, bar_width, bar_height, 1)

        oled.show()

        # Update ball position
        ball_x += ball_x_speed
        ball_y += ball_y_speed

        # Handle bottom bar movement
        if right.value() == 0:
            bar_x += bar_x_speed
            if bar_x + bar_width > WIDTH:
                bar_x = WIDTH - bar_width
        elif left.value() == 0:
            bar_x -= bar_x_speed
            if bar_x < 0:
                bar_x = 0

        # Handle top bar movement
        if right.value() == 0:
            top_bar_x += bar_x_speed
            if top_bar_x + bar_width > WIDTH:
                top_bar_x = WIDTH - bar_width
        elif left.value() == 0:
            top_bar_x -= bar_x_speed
            if top_bar_x < 0:
                top_bar_x = 0

        # Ball collision with walls
        if ball_x <= 0 or ball_x >= WIDTH - 5:
            ball_x_speed = -ball_x_speed

        # Ball collision with bars
        if (ball_y + ball_height >= bar_y and bar_x <= ball_x <= bar_x + bar_width) or \
           (ball_y <= bar_height and top_bar_x <= ball_x <= top_bar_x + bar_width):
            ball_y_speed = -ball_y_speed

            # Randomize ball speed
            if ball_x_speed < 0:
                ball_x_speed = random.randint(-4, -1)
            else:
                ball_x_speed = random.randint(1, 4)

            Score += 1

        # End game if ball touches top or bottom screen edges
        if ball_y < 0 and not (top_bar_x <= ball_x <= top_bar_x + bar_width):
            run = False
        elif ball_y >= HEIGHT - 5 and not (bar_x <= ball_x <= bar_x + bar_width):
            run = False

        time.sleep(0.05)

    # Game over screen
    oled.fill(0)
    oled.text("Game Over", 32, 32)
    oled.text(f"Score: {Score}", 32, 50)
    oled.show()
    time.sleep(5)
    


#main menu method
def main():
    current_selection = 0  # 0 for "Classic", 1 for "Two Lane"
    options = ["Classic", "Caged"]

    while True:
        oled.fill(0)
        
        # Display menu options
        oled.text("Classic", 35, 5)
        oled.text("Caged", 40, 55)
        
        # Draw selector rectangle
        if current_selection == 0:
            oled.rect(30, 3, 70, 12, 1)  # Rectangle around "Classic"
        elif current_selection == 1:
            oled.rect(35, 52, 50, 12, 1)  # Rectangle around "Two Lane"
        
        oled.show()

        # Wait for button presses
        if up.value() == 0:  # Move selection up
            if(current_selection == 1):
                current_selection = 0
                time.sleep(.2)
            elif(current_selection == 0):
                current_selection = 1
                time.sleep(.2)

        elif down.value() == 0:  # Move selection down
            if(current_selection == 0):
                current_selection = 1
                time.sleep(.2)

        elif button1.value() == 0:  # Select option
            if(current_selection == 1):
                oled.fill(0)
                oled.text("Play Caged?", 20, 5)
                oled.text(" A - Yes", 30, 30)
                oled.text("B - No", 40, 50)
                oled.show()
                
                time.sleep(1)
                play = False
                choosing = True
                while choosing:
                    if button1.value() == 0:
                        play = True
                        choosing = False
                    elif button2.value() == 0:
                        choosing = False
                if play:
                    caged()
                
            if current_selection == 0:
                
                oled.fill(0)
                oled.text("Play Classic?", 20, 5)
                oled.text(" A - Yes", 30, 30)
                oled.text("B - No", 40, 50)
                oled.show()
                
                time.sleep(1)
                play = False
                choosing = True
                while choosing:
                    if button1.value() == 0:
                        play = True
                        choosing = False
                    elif button2.value() == 0:
                        choosing = False
                if play:
                    game_mode_1()


# Entry point
if __name__ == "__main__":
    main()
