#!/bin/bash

if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    MONITOR=$m polybar -c ~/.config/polybar/desktops.conf &
    MONITOR=$m polybar -c ~/.config/polybar/system.conf &
  done
else
  polybar -c ~/.config/polybar/desktops.conf &
  polybar -c ~/.config/polybar/system.conf &
fi