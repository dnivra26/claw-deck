# claw-deck

Elgato Stream Deck MK.2 scripts to control [Claude Code](https://claude.ai/code) running in iTerm.

## Layout

```
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│ Accept  │ Reject  │ Cancel  │  Undo   │  Voice  │
│   ✓ Y   │  ✗ Esc  │  Ctrl+C │  /undo  │ /voice  │
├─────────┼─────────┼─────────┼─────────┼─────────┤
│  Plan   │  YOLO   │ Default │  Fast   │Thinking │
│  /plan  │ Shift+⇥ │ Shift+⇥ │  ⌘+O   │  ⌘+T    │
├─────────┼─────────┼─────────┼─────────┼─────────┤
│ Compact │ Review  │ Commit  │  Clear  │ Model   │
│/compact │ /review │ /commit │ /clear  │  ⌘+P    │
└─────────┴─────────┴─────────┴─────────┴─────────┘
```

## Scripts

| # | Button | Script | What it does |
|---|--------|--------|-------------|
| 1 | Accept | `01-accept.sh` | Confirm/accept a tool use |
| 2 | Reject | `02-reject.sh` | Decline a tool use |
| 3 | Cancel | `03-cancel.sh` | Interrupt current operation |
| 4 | Undo | `04-undo.sh` | Revert the last file change |
| 5 | Voice | `05-voice.sh` | Start voice input |
| 6 | Plan | `06-plan-mode.sh` | Enter plan mode (think without executing) |
| 7 | YOLO | `07-yolo-mode.sh` | Cycle permission mode toward Auto |
| 8 | Default | `08-default-mode.sh` | Cycle permission mode toward Default |
| 9 | Fast | `09-fast-mode.sh` | Toggle fast mode |
| 10 | Thinking | `10-thinking.sh` | Toggle extended thinking |
| 11 | Compact | `11-compact.sh` | Compress conversation to save context |
| 12 | Review | `12-review.sh` | Review all changes made this session |
| 13 | Commit | `13-commit.sh` | Commit changes with generated message |
| 14 | Clear | `14-clear.sh` | Clear conversation |
| 15 | Model | `15-model-picker.sh` | Switch between Opus / Sonnet / Haiku |

## Setup

1. Clone this repo
2. Open the Elgato Stream Deck app
3. For each button, drag a **System: Open** action onto the key
4. Set the path to the corresponding script, e.g. `/path/to/claw-deck/scripts/01-accept.sh`

## How it works

Each script uses AppleScript to either:
- **Send keystrokes** to iTerm via System Events (for hotkeys like `Ctrl+C`, `⌘+T`)
- **Write text** to the current iTerm session (for slash commands like `/plan`, `/voice`)

Scripts that send keystrokes will activate (focus) iTerm first. Scripts that write text work via iTerm's scripting API and don't require focus.

## Notes

- Built for **iTerm**. For Terminal.app or other terminals, replace `"iTerm"` in the scripts.
- **YOLO / Default** both cycle the same permission ring (`Shift+Tab`). Press until the footer shows the mode you want.
- Modes cycle: default → acceptEdits → plan → auto.
