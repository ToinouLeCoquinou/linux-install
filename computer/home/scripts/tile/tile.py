import argparse
import subprocess
import re
from dataclasses import dataclass


@dataclass
class WindowProperties:
    id: str
    x:  int
    y:  int
    w:  int
    h:  int


@dataclass
class ScreenProperties:
    id:         str
    x:          int
    y:          int
    w:          int
    h:          int
    menu_bar:   int

# cmd = ['wmctrl', '-i', '-r', get_active_window_id(), '-e', f'1,3840,0,500,500']


def get_window_properties():
    # retieve the window id from xdotool
    xdo_id = subprocess.check_output(['xdotool', 'getactivewindow']).decode().strip()
    win_info = subprocess.check_output(['xwininfo', '-id', xdo_id]).decode()
    print(win_info)

    x = int(re.findall('Absolute upper-left X:  (\\d*)', win_info)[0])
    y = int(re.findall('Absolute upper-left Y:  (\\d*)', win_info)[0])
    w = int(re.findall('Width: (\\d*)', win_info)[0])
    h = int(re.findall('Height: (\\d*)', win_info)[0])

    return WindowProperties(id=xdo_id, x=x, y=y, w=w, h=h)


def get_window_position():
    return 1


def get_window_size():
    return 1


def get_new_window_position():
    return 1


def get_new_window_size():
    return 1


def set_new_window_position(x, y, w, h):
    cmd = ['wmctrl', '-i', '-r', get_active_window_id(), '-e', f'1,3840,0,500,500']
    return subprocess.check_output(cmd)


def set_new_window_size():
    return 1


def move_window(win_prop, direction):
    print(direction)
    print(win_prop)


def resize_window(win_prop, direction):
    print(direction)
    print(win_prop)


if __name__ == '__main__':
    # parse the actions
    parser = argparse.ArgumentParser()
    parser.add_argument("action",
                        choices=['mup', 'mdown', 'mleft', 'mright', 'rup', 'rdown', 'rleft', 'rright',
                                 'setmenubar',],
                        help="The direction where the window will move or will be resized.")
    args = parser.parse_args()

    screen_prop = ScreenProperties('toto', 0, 0, 0, 0, 0)
    win_prop = get_window_properties()

    # switch from the actions parsed to the right method to move or resize
    if args.action[0] == 'm':
        print('move')
        move_window(win_prop, args.action[1:])
    elif args.action[0] == 'r':
        print('resize')
        resize_window(win_prop, args.action[1:])
