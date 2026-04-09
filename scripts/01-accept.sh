#!/bin/bash
# Row 1 | Accept/confirm current tool use
osascript -e '
tell application "iTerm" to activate
delay 0.1
tell application "System Events"
    keystroke "y"
end tell'
