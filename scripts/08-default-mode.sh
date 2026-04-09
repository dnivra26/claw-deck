#!/bin/bash
# Row 2 | Cycle permission mode forward (toward Default)
# Modes cycle: default → acceptEdits → plan → auto
# Press repeatedly until you see "default" in the footer
osascript -e '
tell application "iTerm" to activate
delay 0.1
tell application "System Events"
    key code 48 using shift down -- Shift+Tab
end tell'
