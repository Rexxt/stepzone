from types import CoroutineType
import keyboard
import sys
import os
import time
import cursor
import atexit
import math
from colorama import init
init()

atexit.register(cursor.show)

cursor.hide()
scene = ["game"]
startTime = 0
currentTime = 0
judge = None
tick = 0
BPM = 100
MPB = 1/BPM
MSPB = MPB*60*1000
judgenames = ["PERFECT", "GREAT", "GOOD", "BAD", "POOR"]
judgecolors = [93, 32, 34, 35, 31]
snapcolors = [31, 33, 34, 33]
combo = 0
lanes = [
    [[4,0],[8,0],[12,0],[16,0]],
    [[5,0],[9,0],[13,0],[17,0]],
    [[6,0],[10,0],[14,0],[18,0]],
    [[7,0],[11,0],[15,0],[19,3]]
]
keys = ['d', 'f', 'j', 'k']
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
    tick = math.floor(currentTime/(MSPB/4))
    for i in range(0, len(keys)):
        printXY(3, 6+i, "o" if keyboard.is_pressed(keys[i]) else "O")
    for i in range(0,4):
        if keyboard.is_pressed(keys[i]):
            keyTicks[i] += 1
        else:
            keyTicks[i] = 0
    if judge != None: printXY(3, 15, f'\033[{judgecolors[judge]}m' +  judgenames[judge] + '\033[39m')
    if combo > 0: printXY(4, 15, '\033[32m' + str(combo) + " COMBO" + '\033[39m')
    for ln in range(0, len(lanes)):
        for note in range(0, len(lanes[ln])):
            if note >= noteIndices[ln] and not lanes[ln][note][1]: printXY(3+math.floor(lanes[ln][note][0]-tick), 6+ln, f'\033[{snapcolors[lanes[ln][note][0]%4]}m' + "●" + '\033[39m')
    for ln in range(0, len(lanes)):
        for note in range(0, len(lanes[ln])):
            if note >= noteIndices[ln] and lanes[ln][note][1]:
                printXY(3+math.floor(lanes[ln][note][0]-tick), 6+ln, f'\033[{snapcolors[lanes[ln][note][0]%4]}m' + "▄" + '\033[39m')
                for tail in range(lanes[ln][note][0] + 1, lanes[ln][note][0] + lanes[ln][note][1]): 
                    printXY(3+tail-tick, 6+ln, "\033[32m" + "█" + '\033[39m')
                printXY(3+math.floor(lanes[ln][note][0]+lanes[ln][note][1]-tick), 6+ln, f'\033[{snapcolors[lanes[ln][note][0]%4]}m' + "▀" + '\033[39m')
    for ln in range(0, len(lanes)):
        if keyTicks[ln] == 1 and noteIndices[ln] <= len(lanes[ln]):
            abstime = abs(currentTime - lanes[ln][noteIndices[ln]][0]*MSPB)
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
            print(abstime)
exit()