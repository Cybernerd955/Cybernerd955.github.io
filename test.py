import random
import time
import keyboard
def append_random_numbers_to_file(file_path):
    # Generate three random integers
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = random.randint(1, 100)

    # Format them as X,Y,Z
    new_line = f"{x},{y},{z}\n"

    # Open the file in append mode and write the new line
    with open(file_path, 'a') as file:
        file.write(new_line)

    print(f"Added line: {new_line.strip()} to {file_path}")

# Specify the path to the existing file (e.g., 'data.txt')
file_path = 'data.txt'


# Call the function to append random numbers
while True:
    if keyboard.is_pressed('esc'):  # Stop the loop if 'Esc' is pressed
        print("ESC pressed, exiting the loop.")
        break
    append_random_numbers_to_file(file_path)
    time.sleep(2)
