#!/bin/bash
# Row 2 | Cycle permission mode forward (toward Default)
# Modes cycle: default → acceptEdits → plan → auto
# Sends Escape then [Z which is the terminal escape sequence for Shift+Tab
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text (ASCII character 27) & "[Z" without newline
    end tell
end tell'
