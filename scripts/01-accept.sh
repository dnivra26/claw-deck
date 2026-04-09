#!/bin/bash
# Row 1 | Accept/confirm current tool use
# Sends "y" followed by newline — works for confirmation dialogs
osascript -e '
tell application "iTerm"
    tell current session of current window
        write text "y"
    end tell
end tell'
