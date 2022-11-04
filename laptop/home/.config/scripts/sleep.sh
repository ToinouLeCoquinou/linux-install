#!/bin/bash

status="$(xset q)"
device=8

xinput --disable $device

sleep 1
xset dpms force off

while true; do
  status=$(xset q | grep -o "^\s*Monitor is .*" | grep -o -e On -e Off)
  if [[ $status == "On" ]]; then
    xinput --enable $device
    exit 0
  fi
  sleep 1
done
