# up-bot

Upbot is a python3 script that automatically sends a message to a chat on the Signal Messenger desktop client within a randomized window of time, on selected days of the week.


## Usage:
1. Install python and required packages (see imports in upbot.py)
2. Open command prompt/terminal
3. Run script, use -h for help with syntax
4. Minimize command prompt winow (unless you want to look at it do nothing)
5. Open signal chat (on main monitor if multi-monitor setup) and click on the chat the message will be sent to, then minimize signal.
6. Adjust ratio settings in script to fit your monitor (must be main monitor, pyautogui does not support multiple monitors)
7. Sleep in peace

## Options:
- **w**:   Window of time plus or minus the set time to send the message. It will send randomly within the window. In in hours if time is HH, in minutes if time is HH:MM, in seconds if time is HH:MM:SS
- **t**:      Time for the message to be sent in HH:MM:SS format (can send only HH or HH:MM if desired)
- **m**:      Message to be sent. Needs double quotation marks surrounding it if the message is more than one word.
- **M,T,W,H,F,S,U**:     Day of the week where H=Thursday and U=Sunday. Python's getopt does not support multi-letter options.

## Compatability:
 - Only works on Windows (pygetwindow compatability)
 - If there are multiple monitors, Signal must maximize when clicked to the main monitor (pyautogui compatability)
 - Signal must have pre-selected the chat that message will be sent to (or it may send to wrong chat)
 - Make sure no other programs are running with "Signal" in the name, or it may try to send the message to the wrong window

