# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
import subprocess


def get_active_window_id():
    return subprocess.check_output(['xdotool', 'getactivewindow']).decode().strip()


def move_resize_window(x, y, w, h):
    cmd = ['wmctrl', '-i', '-r', get_active_window_id(), '-e', f'1,3840,0,500,500']
    return subprocess.check_output(cmd)


def get_window_position():
    return 1


def get_window_size():
    return 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("direction",
                        choices=['up', 'down', 'left', 'right'],
                        help="The direction where the window will move or will be resize.")
    args = parser.parse_args()

    print(args.direction)

    win_info = subprocess.check_output(['xwininfo', '-id', get_active_window_id()]).decode()
    print(win_info)

