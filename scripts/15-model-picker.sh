#!/bin/bash
# Row 3 | Open model picker (Opus/Sonnet/Haiku)
osascript -e '
tell application "iTerm" to activate
delay 0.1
tell application "System Events"
    keystroke "p" using command down
end tell'
