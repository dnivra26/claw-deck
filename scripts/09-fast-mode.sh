#!/bin/bash
# Row 2 | Toggle fast mode (Cmd+O → Escape then o in terminal)
# Uses iTerm's proprietary escape sequence for Cmd+key
# CSI > 2 ; <keycode> ~ sends Cmd+key in iTerm
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text (ASCII character 27) & "o" without newline
    end tell
end tell'
