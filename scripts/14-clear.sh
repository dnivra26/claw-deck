#!/bin/bash
# Row 3 | Clear conversation and start fresh
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text "/clear"
    end tell
end tell'
