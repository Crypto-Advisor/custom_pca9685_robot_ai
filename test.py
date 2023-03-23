import keyboard

def main():
    while True:
        if keyboard.is_pressed('w'):
            while keyboard.is_pressed('w'):
                print('forward')
            #default motor speed
            print('Default')

        elif keyboard.is_pressed('s'):
            print('backward')
            # backward()
        
        if keyboard.is_pressed('a'):
            print('left')
            # turn_left()
        elif keyboard.is_pressed('d'):
            print('right')
            # turn_right()
    
main()