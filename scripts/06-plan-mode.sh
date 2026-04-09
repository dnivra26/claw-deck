#!/bin/bash
# Row 2 | Enter plan mode (think without executing)
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text "/plan"
    end tell
end tell'
