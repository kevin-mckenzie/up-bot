import pyautogui as pag
import pygetwindow as pgw
from time import sleep
import getopt
from sys import argv
import schedule
from random import randint

'''
Upbot is a python3 script that automatically sends a message to a chat on the Signal Messenger desktop client within a randomized window of time, on selected days of the week.


See README.md at https://github.com/kevin-mckenzie/up-bot for usage and compatability.
'''

#Adjust ratios to fit personal monitor/toolbar settings
VERTICAL_RATIO  = 15 / 16 #Ratio of screen starting from top to where Signal text bar is
HORIZONAL_RATIO = 1 / 2   #Center of screen, location of text bar

#Default message and time
MESSAGE = "Up"

def up():
    #Wake up computer
    pag.typewrite("\n")
    sleep(1)
    pag.typewrite("\n")
    sleep(2)

    #Find Signal, assumes it is the only window with "Signal" in the name
    signal = pgw.getWindowsWithTitle("Signal")[0]
    signal.activate() #Select window
    signal.maximize() #Maximize
    x, y = pag.size() #Get screen size
    #Move mouse to location of text bar at bottom of signal, this may vary on different monitors/windows settings (e.g. larger icon bar)
    pag.moveTo((x * HORIZONAL_RATIO), (y * VERTICAL_RATIO), duration=0)
    pag.click() #Click on text bar
    pag.typewrite(f"{MESSAGE}\n") #Send message
    signal.minimize() #Minimize signal window

def printusage():
    print("Usage: python3 upbot.py [-t <time of day (e.g. 13:30)>] [-m <message to send>] [-h (get help)] {[-M] [-T] [-W] [-H(Thursday)] [-F] [-S] [-U(Sunday)] (days of the week)}")
    print("Days of the week options must come AFTER options or time, window, and message settings may not be properly applied.")

#Function that randomizes time within a window of minutes
#If window goes above or below the hour mark, it rounds to the hour it would have passed
def randomize_time(old_time, mins_w):
    try:
        min_int = int(old_time[-2:])
        hi = min_int + mins_w
        lo = min_int - mins_w
        if hi > 59:
            hi = 59
        if lo < 0:
            lo = 0
        
        new_mins = str(randint(lo, hi)).rjust(2, "0")
        new_time = old_time[:-2] + new_mins

        return new_time
    except ValueError:
        print("Could not adjust window.")
        return old_time


def main():
    #set default time window and time to send message
    w = 0
    TIME = "05:30"

    #TODO: Add longopts for more intuitive day of the week entry
    opts, args = getopt.getopt(argv[1:], "ht:m:w:MTWHFSU")

    #times are adjusted by +- window for each day of the week
    #However, the time for a given day week to week will be the same because of how job definition works
    try:
        for o, a in opts:
            if o == '-h':
                printusage()
                return
            elif o == '-t':
                TIME = a
            elif o == '-m':
                global MESSAGE
                MESSAGE = a
            elif o == '-w':
                try:
                    w = int(a)
                except ValueError:
                    print("Invalid window, applying default 0 minute adjustment.")
                    w = 0
            elif o == '-M':
                schedule.every().monday.at(randomize_time(TIME, w)).do(up)
            elif o == '-T':
                schedule.every().tuesday.at(randomize_time(TIME, w)).do(up)
            elif o == '-W':
                schedule.every().wednesday.at(randomize_time(TIME, w)).do(up)
            elif o == '-H':
                schedule.every().thursday.at(randomize_time(TIME, w)).do(up)
            elif o == '-F':
                schedule.every().friday.at(randomize_time(TIME, w)).do(up)
            elif o == '-S':
                schedule.every().saturday.at(randomize_time(TIME, w)).do(up)
            elif o == '-U':
                schedule.every().sunday.at(randomize_time(TIME, w)).do(up)
            else:
                print("Invalid option")
                printusage()
                return
    except schedule.ScheduleValueError:
        print("Invalid time format (valid format is HH:MM")
        printusage()
        return
        

    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == "__main__":
    main()
