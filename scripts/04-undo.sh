#!/bin/bash
# Row 1 | Undo the last file change Claude made
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text "/undo"
    end tell
end tell'
