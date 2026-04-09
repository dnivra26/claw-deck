#!/bin/bash
# Row 1 | Start voice input mode
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text "/voice"
    end tell
end tell'
