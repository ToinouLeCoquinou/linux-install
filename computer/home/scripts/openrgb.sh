#!/bin/bash

FILE=~/.config/OpenRGB/OpenRGB.json
if [ -f "$FILE" ]; then
    rm $FILE
fi
openrgb -c $1
