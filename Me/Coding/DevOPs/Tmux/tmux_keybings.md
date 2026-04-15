##### =========================================================
##### TMUX CHEATSHEET (Navigation + Sessions + Persistence)
##### Prefix = Ctrl+b
##### =========================================================

##### -------------------------------
##### Session lifecycle (most used)
##### -------------------------------

# Create a NEW named session (outside tmux)
# tmux new -s dev
# tmux new -s dev -d          -> create detached

# List sessions (outside tmux)
# tmux ls

# Attach to a session (outside tmux)
# tmux a -t dev
# tmux a                      -> attach last session

# Detach (inside tmux)
# Ctrl+b d

# Rename current session (inside tmux)
# Ctrl+b $

# Rename session (outside tmux)
# tmux rename-session -t oldname newname

# Kill session (outside tmux)
# tmux kill-session -t dev

# Kill server (DANGER: kills ALL sessions)
# tmux kill-server

# Switch sessions (inside tmux)
# Ctrl+b (                    -> previous session
# Ctrl+b )                    -> next session
# Ctrl+b s                    -> choose session interactively

# Show current session name in status bar token:

##### -------------------------------
##### Windows (tabs)
##### -------------------------------

# New window
# Ctrl+b c

# Rename window
# Ctrl+b ,

# Next / previous window
# Ctrl+b n
# Ctrl+b p

# Jump to window number
# Ctrl+b <1-9>

# Interactive window list
# Ctrl+b w

# Kill window (confirm)
# Ctrl+b &

##### -------------------------------
##### Panes (splits)
##### -------------------------------

# Split panes
# Ctrl+b %                    -> vertical split (left/right)
# Ctrl+b "                    -> horizontal split (top/bottom)

# Move between panes
# Ctrl+b arrows

# Show pane numbers + jump
# Ctrl+b q

# Kill pane (confirm)
# Ctrl+b x

# Zoom/unzoom current pane
# Ctrl+b z

# Break pane into a new window
# Ctrl+b !

# Swap panes
# Ctrl+b {                    -> swap with previous
# Ctrl+b }                    -> swap with next

##### -------------------------------
##### Layouts / Resize
##### -------------------------------

# Cycle layouts
# Ctrl+b Space

# Resize pane (fine control)
# Ctrl+b Ctrl+←/→/↑/↓

##### -------------------------------
##### Copy mode (scrollback)
##### -------------------------------

# Enter copy mode
# Ctrl+b [

# Quit copy mode
# q

# Select/copy
# Space                        -> start selection
# Enter                        -> copy selection

##### -------------------------------
##### Usually-used misc commands
##### -------------------------------

# Display all keybindings
# Ctrl+b ?

# Command prompt
# Ctrl+b :

# Show clock
# Ctrl+b t

# Redraw client (fix visual glitches)
# Ctrl+b r

# Display tmux messages / last status message
# Ctrl+b ~

# Reload config (inside tmux)
# Ctrl+b : source-file ~/.tmux.conf

##### -------------------------------
##### TPM / RESURRECT / CONTINUUM
##### -------------------------------

# TPM plugin actions
# Ctrl+b I                    -> install plugins
# Ctrl+b U                    -> update plugins
# Ctrl+b alt+u                -> remove plugins

# tmux-resurrect
# Ctrl+b Ctrl+s               -> save sessions/windows/panes state
# Ctrl+b Ctrl+r               -> restore state

# Notes:
# - resurrect restores layout + commands, NOT full program memory state
# - long-running services should be systemd, tmux is not a service manager

# tmux-continuum
# - auto-saves periodically (commonly every 15 mins if configured)
# - can auto-restore on tmux start when enabled:
#   set -g @continuum-restore 'on'

