#!/bin/bash
# Row 3 | Open model picker (Cmd+P)
# Sends Meta+P (Escape then p) which maps to model picker
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text (ASCII character 27) & "p" without newline
    end tell
end tell'
