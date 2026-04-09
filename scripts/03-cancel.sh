#!/bin/bash
# Row 1 | Cancel/interrupt current operation
osascript -e '
tell application "iTerm" to activate
delay 0.1
tell application "System Events"
    keystroke "c" using control down
end tell'
