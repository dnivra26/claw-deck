#!/bin/bash
# Row 3 | Commit changes with Claude-generated message
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text "/commit"
    end tell
end tell'
