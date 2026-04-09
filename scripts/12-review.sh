#!/bin/bash
# Row 3 | Review all changes Claude has made this session
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text "/review"
    end tell
end tell'
