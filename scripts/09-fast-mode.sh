#!/bin/bash
# Row 2 | Toggle fast mode on/off
osascript -e '
tell application "iTerm" to activate
delay 0.1
tell application "System Events"
    keystroke "o" using command down
end tell'
