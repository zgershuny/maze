import time

# Introduction
name = input("Welcome to the maze, adventurer. What is your name?")

print(name, ", you have a compass with you. Use it well to guide you.")
print("Enter 'w' to go west, 'n' to go north, 'e' to go east, or 's' to go south.")
print("Good luck!")
time.sleep(2)

print("You enter the maze. The door slams behind you.")


# Prompt for directions
def directions():
    ans = ''
    while ans != 'n' and ans != 's' and ans != 'w' and ans != 'e':
        ans = input("Which way will you go?")
        if ans != 'n' and ans != 's' and ans != 'w' and ans != 'e':
            print("That is not a direction.")
            ans = input("Which way will you go?")
        return ans


# Fork Rooms

def fork0():
    print("There is a door to the north, east, and south.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 's':
            room0()
        elif next_room == 'n':
            room1()
        elif next_room == 'e':
            room3()
        else:
            print("There is no door.")


def fork1():
    print("There is a door to the north, west, and south.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'n':
            fork2()
        elif next_room == 's':
            room5()
        elif next_room == 'w':
            room3()
        else:
            print("There is no door.")


def fork2():
    print("There is a door to the west, east, and south.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'w':
            dead_end1()
        elif next_room == 'e':
            room7()
        elif next_room == 's':
            fork1()
        else:
            print("There is no door.")


# Dead Ends

def dead_end0():
    print("Oh no. It is a dead end.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'w':
            room0()
        else:
            print("There is no door.")


def dead_end1():
    print("Oh no. It is a dead end.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'e':
            fork2()
        else:
            print("There is no door.")


def dead_end2():
    print("Oh no. It is a dead end.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'w':
            room4()
        else:
            print("There is no door.")


def dead_end3():
    print("Oh no. It is a dead end.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 's':
            room6()
        else:
            print("There is no door.")


# Single Path Rooms

# Rooms on the correct path
def room0():
    print("There is a door to the north and to the east.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'e':
            dead_end0()
        elif next_room == 'n':
            fork0()
        elif next_room == 's':
            print("The door is shut.")
        else:
            print("There is no door there.")


def room3():
    print("There is a door to the west and to the east.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'w':
            fork0()
        elif next_room == 'e':
            fork1()
        else:
            print("There is no door.")


def room7():
    print("There is a door to the north and to the east.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'e':
            fork2()
        elif next_room == 'n':
            room8()
        else:
            print("There is no door.")

    # Rooms on the incorrect path


def room1():
    print("There is a door to the north and to the south.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 's':
            fork0()
        elif next_room == 'n':
            room2()
        else:
            print("There is no door.")


def room2():
    print("There is a door to the east and to the south.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 's':
            room1()
        elif next_room == 'e':
            room4()
        else:
            print("There is no door.")


def room4():
    print("There is a door to the west and east.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'w':
            room2()
        elif next_room == 'e':
            dead_end2()
        else:
            print("There is no door.")


def room5():
    print("There is a door to the north and to the east.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'e':
            room6()
        elif next_room == 'n':
            fork1()
        else:
            print("There is no door.")


def room6():
    print("There is a door to the north and west.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'w':
            room5()
        elif next_room == 'n':
            dead_end3()
        else:
            print("There is no door.")


# Final Room
def room8():
    print("There is a door to the north and to the south.")
    next_room = ''
    while next_room != 'n' or next_room != 's' or next_room != 'w' or next_room != 'e':
        next_room = directions()
        if next_room == 'n':  # End Game
            print("Congratulations, " + name + ". You completed the maze!")
            exit(0)
        elif next_room == 's':
            room7()
        else:
            print("There is no door.")


# Start Game


room0()
