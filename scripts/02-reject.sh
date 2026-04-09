#!/bin/bash
# Row 1 | Reject/decline current tool use
# Sends Escape character (ASCII 27)
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text (ASCII character 27)
    end tell
end tell'
