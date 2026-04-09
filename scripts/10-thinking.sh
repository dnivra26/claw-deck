#!/bin/bash
# Row 2 | Toggle extended thinking (Cmd+T)
# Sends Meta+T (Escape then t) which maps to the thinking toggle
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text (ASCII character 27) & "t" without newline
    end tell
end tell'
