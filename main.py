from types import CoroutineType
import keyboard
import sys
import os
import time
import cursor
import atexit
from colorama import init
init()

atexit.register(cursor.show)

cursor.hide()
startTime = 0
currentTime = 0
judge = None
tick = 0
BPM = 15
MPB = 1/BPM
MSPB = MPB*60*1000
judgenames = ["PERFECT", "GREAT", "GOOD", "BAD", "POOR"]
judgecolors = ['93','32','34','35','31']
combo = 0
lanes = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
noteIndices = [0,0,0,0]
keyTicks = [0,0,0,0]
counts = [0,0,0,0,0]

def current_milli_time():
    return round(time.time() * 1000)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printXY(x, y, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()

startTime = current_milli_time()
while True:
    clear()
    currentTime = current_milli_time() - startTime
    tick = currentTime/(MSPB/4)
    printXY(3, 6, "o" if keyboard.is_pressed('d') else "O")
    printXY(3, 7, "o" if keyboard.is_pressed('f') else "O")
    printXY(3, 8, "o" if keyboard.is_pressed('j') else "O")
    printXY(3, 9, "o" if keyboard.is_pressed('k') else "O")
    for i in range(0,4):
        v = ['d', 'f', 'j', 'k']
        if keyboard.is_pressed(v[i]):
            keyTicks[i] += 1
        else:
            keyTicks[i] = 0
    if judge != None: printXY(3, 15, f'\033[{judgecolors[judge]}m' +  judgenames[judge] + '\033[39m')
    if combo > 0: printXY(4, 15, '\033[32m' + str(combo) + " COMBO" + '\033[39m')
    for ln in range(0, len(lanes)):
        for note in range(0, len(lanes[ln])):
            if note >= noteIndices[ln]: printXY(3+lanes[ln][note]-tick, 6+ln, "●")
    for ln in range(0, len(lanes)):
        if keyTicks[ln] == 1 and noteIndices[ln] <= len(lanes[ln]):
            abstime = abs(currentTime - lanes[ln][noteIndices[ln]]*MSPB)
            if abstime <= 180:
                if abstime <= 22:
                    judge = 0
                    combo += 1
                    counts[judge] += 1
                    noteIndices[ln] = min(noteIndices[ln] + 1, len(lanes[ln]))
                elif abstime <= 45:
                    judge = 1
                    combo += 1
                    counts[judge] += 1
                    noteIndices[ln] += min(noteIndices[ln] + 1, len(lanes[ln]))
                elif abstime <= 90:
                    judge = 2
                    combo += 1
                    counts[judge] += 1
                    noteIndices[ln] += min(noteIndices[ln] + 1, len(lanes[ln]))
                elif abstime <= 135:
                    judge = 3
                    combo = 0
                    counts[judge] += 1
                    noteIndices[ln] += min(noteIndices[ln] + 1, len(lanes[ln]))
                else:
                    judge = 4
                    combo = 0
                    counts[judge] += 1
                    noteIndices[ln] += min(noteIndices[ln] + 1, len(lanes[ln]))
    print(MSPB)
exit()