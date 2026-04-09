#!/bin/bash
# Row 2 | Toggle extended thinking on/off
osascript -e '
tell application "iTerm" to activate
delay 0.1
tell application "System Events"
    keystroke "t" using command down
end tell'
