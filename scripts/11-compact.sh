#!/bin/bash
# Row 3 | Compact conversation to save context window
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text "/compact"
    end tell
end tell'
