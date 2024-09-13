#!/usr/bin/python

import argparse
import subprocess
import re
from dataclasses import dataclass


margin = 18
bottom_bar = 34
windows_w = 1256
windows_h = 1036


@dataclass
class WindowProperties:
    id: str
    x: int
    y: int
    w: int
    h: int

def get_window_properties():
    # retieve the window id from xdotool
    xdo_id = subprocess.check_output(['xdotool', 'getactivewindow']).decode().strip()
    win_info = subprocess.check_output(['xwininfo', '-id', xdo_id]).decode()

    x = int(re.findall('Absolute upper-left X: {2}(\\d*)', win_info)[0])
    y = int(re.findall('Absolute upper-left Y: {2}(\\d*)', win_info)[0])
    w = int(re.findall('Width: (\\d*)', win_info)[0])
    h = int(re.findall('Height: (\\d*)', win_info)[0])

    return WindowProperties(id=xdo_id, x=x, y=y, w=w, h=h)

def set_new_window_parameters(x, y, w, h):
    cmd = ['wmctrl', '-i', '-r', win_prop.id, '-e', f'1,' + str(x) + ',' + str(y) + ',' + str(w) + ',' + str(h) + '']

    return subprocess.check_output(cmd)

def move_window(direction):
    zone_w = win_prop.x // 1280
    zone_h = win_prop.y // (1080 - bottom_bar)
    new_x, new_y = win_prop.x, win_prop.y

    print("win_prop.x: " + str(win_prop.x))
    print("zone_w: " + str(zone_w))
    print("win_prop.y: " + str(win_prop.y))
    print("zone_h: " + str(zone_h))
    match direction:
        case 'left':
            if 0 <= zone_w < 3:
                if win_prop.x > (zone_w * windows_w) + (zone_w + 1) * margin:
                    print("test: 0")
                    new_x = (zone_w * windows_w) + (zone_w + 1) * margin
                elif win_prop.x <= (zone_w * windows_w) + (zone_w + 1) * margin:
                    if zone_w == 0:
                        print("test: 1")
                        new_x = 11 * margin + 8 * windows_w
                    else:
                        print("test: 2")
                        new_x = (zone_w - 1) * windows_w + zone_w * margin
            elif 3 <= zone_w < 6:
                if win_prop.x > margin + (zone_w * windows_w) + (zone_w + 1) * margin:
                    print("test: 3")
                    new_x = margin + (zone_w * windows_w) + (zone_w + 1) * margin
                elif win_prop.x <= margin + (zone_w * windows_w) + (zone_w + 1) * margin:
                    if zone_w == 3:
                        print("test: 4")
                        new_x = (zone_w - 1) * windows_w + zone_w * margin
                    else:
                        print("test: 5")
                        new_x = margin + (zone_w - 1) * windows_w + zone_w * margin
            elif 6 <= zone_w <= 8:
                if win_prop.x > 2 * margin + (zone_w * windows_w) + (zone_w + 1) * margin:
                    print("test: 6")
                    new_x = 2 * margin + (zone_w * windows_w) + (zone_w + 1) * margin
                elif win_prop.x <= 2 * margin + (zone_w * windows_w) + (zone_w + 1) * margin:
                    if zone_w == 6:
                        print("test: 7")
                        new_x = margin + (zone_w - 1) * windows_w + zone_w * margin
                    else:
                        print("test: 8")
                        new_x = 2 * margin + (zone_w - 1) * windows_w + zone_w * margin
        case 'right':
            new_x = margin + (zone_w + 1) * (windows_w + margin)
            if 2 <= zone_w < 5:
                print("test 9")
                new_x = margin + new_x
            elif 5 <= zone_w < 8:
                print("test 10")
                new_x = 2 * margin + new_x
            elif zone_w == 8:
                new_x = margin
        case 'up':
            if zone_h == 0:
                if win_prop.y > margin:
                    new_y = margin
                elif 0 <= win_prop.y <= margin:
                    new_y = 2 * margin + windows_h
            if zone_h == 1:
                if win_prop.y > 2 * margin + windows_h:
                    new_y = 2 * margin + windows_h
                elif win_prop.y <= 2 * margin + windows_h:
                    new_y = margin
        case 'down':
            if zone_h == 0:
                if win_prop.y >= margin:
                    new_y = 2 * margin + windows_h
                elif 0 <= win_prop.y < margin:
                    new_y = margin
            if zone_h == 1:
                if win_prop.y >= 2 * margin + windows_h:
                    new_y = margin
                elif win_prop.y < 2 * margin + windows_h:
                    new_y = 2 * margin + windows_h


    print("new_x :" + str(new_x))
    print("new_y :" + str(new_y))
    set_new_window_parameters(new_x, new_y, win_prop.w, win_prop.h)


def resize_window(direction):
    new_w, new_h = win_prop.w, win_prop.h
    zone_w = win_prop.x // 1280
    zone_h = win_prop.y // (1080 - bottom_bar)
    print("win_prop.x: " + str(win_prop.x))
    print("win_prop.y: " + str(win_prop.y))

    match direction:
        case 'left':
            if windows_w < win_prop.w <= 2 * windows_w + margin:
                print("test 0")
                new_w = windows_w
            elif 2 * windows_w + margin < win_prop.w <= 3 * windows_w + 2 * margin:
                print("test 1")
                new_w = 2 * windows_w + margin
            elif win_prop.w > 3 * windows_w + 2 * margin:
                print("test 2")
                new_w = 3 * windows_w + 2 * margin
        case 'right':
            if 0 < win_prop.w < windows_w:
                print("test 3")
                new_w = windows_w
            elif ((windows_w <= win_prop.w < 2 * windows_w + margin)
                   and ((zone_w != 2) and (zone_w != 5) and (zone_w != 8))):
                print("test 4")
                new_w = 2 * windows_w + margin
            elif ((2 * windows_w + margin <= win_prop.w < 3 * windows_w + 2 * margin)
                   and ((zone_w != 1) and (zone_w != 4) and (zone_w != 7))):
                print("test 5")
                new_w = 3 * windows_w + 2 * margin
        case 'up':
            if windows_h <= win_prop.h <= 2 * windows_h + margin:
                new_h = windows_h
            elif 2 * windows_h + margin < win_prop.h:
                new_h = 2 * windows_h + margin
        case 'down':
            if 0 < win_prop.h <= windows_h and zone_h != 1:
                new_h = 2 * windows_h + margin

    print("win_prop.x: " + str(win_prop.x))
    print("win_prop.y: " + str(win_prop.y))
    print("new_w: " + str(new_w))
    print("new_h: " + str(new_h))
    set_new_window_parameters(win_prop.x, win_prop.y, new_w, new_h)

if __name__ == '__main__':
    # This script need xdotool and xorg-xwininfo to work…
    # parse the actions

    parser = argparse.ArgumentParser()
    parser.add_argument("action",
                        choices=['mup', 'mdown', 'mleft', 'mright', 'rup', 'rdown', 'rleft', 'rright',
                                 'setmenubar', ],
                        help="The direction where the window will move or will be resized.")
    args = parser.parse_args()

    win_prop = get_window_properties()

    # switch from the actions parsed to the right method to move or resize
    if args.action[0] == 'm':
        print('move')
        move_window(args.action[1:])
    elif args.action[0] == 'r':
        print('resize')
        resize_window(args.action[1:])
