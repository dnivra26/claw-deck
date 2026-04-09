#!/bin/bash
# Row 1 | Cancel/interrupt current operation (Ctrl+C)
# Sends ETX character (ASCII 3 = Ctrl+C)
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text (ASCII character 3)
    end tell
end tell'
