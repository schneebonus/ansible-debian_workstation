#!/bin/sh
# shell script to prepend i3status with more stuff

i3status | while :
do
        read line
        # echo $(python add_brightness.py "$line")
	echo "$line"
done
