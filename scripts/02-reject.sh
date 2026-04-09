#!/bin/bash
# Row 1 | Reject/decline current tool use
osascript -e '
tell application "iTerm" to activate
delay 0.1
tell application "System Events"
    key code 53 -- Escape
end tell'
