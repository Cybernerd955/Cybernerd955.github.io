import time
import keyboard

def press_keys():
    try:
        time.sleep(5)  # Wait for 10 seconds before starting the loop
        while True:
            if keyboard.is_pressed('esc'):  # Stop the loop if 'Esc' is pressed
                print("ESC pressed, exiting the loop.")
                break
            keyboard.press_and_release('g')
            keyboard.press_and_release('i')
            keyboard.press_and_release('t')
            keyboard.press_and_release(' ')
            keyboard.press_and_release('a')
            keyboard.press_and_release('d')
            keyboard.press_and_release('d')
            keyboard.press_and_release(' ')
            keyboard.press_and_release('.')
            keyboard.press_and_release('enter')

            # Command: git commit -m " "
            time.sleep(1)  # Wait for 1 second before typing the next command
            keyboard.press_and_release('g')
            keyboard.press_and_release('i')
            keyboard.press_and_release('t')
            keyboard.press_and_release(' ')
            keyboard.press_and_release('c')
            keyboard.press_and_release('o')
            keyboard.press_and_release('m')
            keyboard.press_and_release('m')
            keyboard.press_and_release('i')
            keyboard.press_and_release('t')
            keyboard.press_and_release(' ')
            keyboard.press_and_release('-')
            keyboard.press_and_release('m')
            keyboard.press_and_release(' ')
            keyboard.press_and_release('"')
            keyboard.press_and_release('1')
            keyboard.press_and_release('"')
            keyboard.press_and_release('enter')

            # Command: git push
            time.sleep(1)  # Wait for 1 second before typing the next command
            keyboard.press_and_release('g')
            keyboard.press_and_release('i')
            keyboard.press_and_release('t')
            keyboard.press_and_release(' ')
            keyboard.press_and_release('p')
            keyboard.press_and_release('u')
            keyboard.press_and_release('s')
            keyboard.press_and_release('h')
            keyboard.press_and_release('enter')
            time.sleep(10)  # Wait 10 second
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    press_keys()

