# up-bot

Compatability:
 - Only works on Windows (pygetwindow compatability)
 - If there are multiple monitors, Signal must maximize to the main monitor (pyautogui compatability)
 - Signal must maximize to the chat that "Up" will be sent to (or it may send to wrong chat)
 - This script assumes that ups are sent Tuesday, Wednesday, and Thursday but this can be adjusted.
 - Make sure no other programs are running with "Signal" in the name, or it will try to send up to the wrong window

Usage:
1. Turn off pin/password when computer wakes from sleep
2. Open command prompt/terminal
3. Run script, use -h for help
4. Minimize command prompt winow
5. Open signal chat (on main monitor) and have the chat you want to send up to selected
6. Adjust ratio settings to fit your monitor (must be main monitor, pyautogui does not support multiple monitors)
7. Sleep in peace
