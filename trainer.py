import random
import sys
import time

NUM_NOTES = 12
MAJOR_SCALE_INTERVALS = [2,2,1,2,2,2,1]

# ENUMs
def enumToNote(num):
    note = "X"
    match num:
        case 0:
            note = "C"
        case 1:
            note = "C#"
        case 2:
            note = "D"
        case 3:
            note = "D#"
        case 4:
            note = "E"
        case 5:
            note = "F"
        case 6:
            note = "F#"
        case 7:
            note = "G"
        case 8:
            note = "G#"
        case 9:
            note = "A"
        case 10:
            note = "A#"
        case 11:
            note = "B"
        
    return note

def noteToEnum(note):
    # Lazy, inefficient, dangerous, but works
    while True:
        num = random.randint(0, NUM_NOTES-1)
        if enumToNote(num) == note:
            return num

    return 0

# Guitar = EADGBE, bass is a subset, just EADG
def numToFret(num, string):
    # Each string is 5 semi-tones apart, so just string * 5
    E_OFFSET = 4
    base = E_OFFSET
    noteNum = base - (string * 5) + ( (num + E_OFFSET) % NUM_NOTES )
    return noteNum % NUM_NOTES

# The nth string on a guitar/bass equates to which string? I'm assuming it's easier to think of the named string rather than the ordered
def numToString(string):
    rtnStr = "X"
    match string:
        case 0:
            rtnStr = "E"
        case 1:
            rtnStr = "A"
        case 2:
            rtnStr = "D"
        case 3:
            rtnStr = "G"
        case 4:
            rtnStr = "B"
        case 5:
            rtnStr = "E upper"
    return rtnStr

def printTabs(num, string, numStrings):
    fret = numToFret(num, string)
    for st in range(numStrings):
        # print("AAA" + str(num))
        print("", end = "")
        # Works in 'inverting it', so it goes from lowest to highest string
        if st == (numStrings - 1 - string):
            if fret > 9:
                print(f"---{fret}--")
            
            else:
                print(f"---{fret}---")
        else:
            print("-------")

def main():
    
    while True:
        inp = input("Input a delay (seconds): ")
        try:
            delay = int(inp)
            break
        except:
            print("Invalid Input")

    numStr = 6
    while True:
        inp = input("Bass or Guitar? (b/g): ")
        if inp == "b":
            numStr = 4
            break
        elif inp == "g":
            numStr = 6
            break
        else:
            print("Invalid input")

    auto = False

    while True:
        print("====================================")
        num = random.randint(0, NUM_NOTES - 1)
        string = random.randint(0, numStr - 1)
        print(f"{enumToNote(num)} on {numToString(string)} string")
        # print(f"{enumToNote(num)} converts to {numToFret(num, string)} on {numToString(string)}")
        time.sleep(delay)
        printTabs(num, string, numStr)

        if not auto:
            while True:
                inp = input("Again? (Y/N/Auto) : ").lower()
                if inp == "y":
                    break
                elif inp == "n":
                    exit()
                elif inp == "a" or inp == "auto":
                    auto = True
                    break
                else:
                    print("Invalid input")
        else:
            time.sleep(1)   # Comment this out if you want real hell
        

if __name__ == "__main__":
    main()