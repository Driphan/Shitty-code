from distutils.command.build_scripts import first_line_re

global entered
entered = True
inventory = ["Piece of Paper"]
global door_open
door_open = False
global door1_open
door1_open = False
global door2_open
door2_open = False
global flashlight_on
flashlight_on = False
global mailbox_open
mailbox_open = False
global flashlight_taken
flashlight_taken = False
global hammer_taken
hammer_taken = False
global key_taken
key_taken = False
global key1_taken
key1_taken = False
global key2_taken
key2_taken = False
global box_smashed
box_smashed = False
global basement_open
basement_open = False
global nails_taken
nails_taken = False
global yarn_taken
yarn_taken = False
global can_taken
can_taken = False
global matchbox_taken
matchbox_taken = False
global candles_on
candles_on = False
global match_on
match_on = False
global screwdriver_taken
screwdriver_taken = False
global rope_taken
rope_taken = False
global crate_open
crate_open = False
global statue_fallen
statue_fallen = False
global safe_open
safe_open = False
global seeds_taken
seeds_taken = False
location_global = "South of House"
print("Welcome to Pumpkin People Paranoia")
print("In order to have maximum success of finding the right inputs input objects as one word and singular.")
print("")
print("These commands might also be helpful: north, south, west, east, up, down, look, examine, take, hit, light, unlock, enter, open, and turn on.")
print("")
print("South of House")
print("You stand in front of an abandoned spooky house, it's intimidating structure towering over your timid frame.")
print("A crisp gust of wind hits you unexpectedly, chilling you to the bone.")
print("You have to get inside the house, the pumpkin people are after you.")
print("The front of the house has a large wooden door, but it is locked shut. There are two windows on either side of the door.")
print("To the side stands an ivy-ridden mailbox.")

def look(location, flashlight_on):
    global entered
    if location == "North of House" and basement_open == False:
        print ("This wall is very spooky, and it has one very spooky basement door.")
    elif location == "North of House":
        print("This wall is especially spooky and has a door that is open.")
    if location == "West of House": 
        print ("Here is a blank wall on the house, it is very spooky.")
    if location == "South of House" and door_open == False: 
        print ("The front of the house has a large wooden door, but it is locked shut. There are two windows on either side of the door.")
    if location == "South of House" and door_open == True: 
        print ("The front of the house has a large wooden door that stands ajar. There are two windows on either side of the door.")
    if location == "East of House":
        print ("This wall is very, very spooky and very, very blank.")
    if location == "Main Basement" and flashlight_on == False:
        print ("You are now in the spooky basement of the spooky house.  It is very dark")
    if location == "Main Basement" and flashlight_on == True:
        print ("You are now in the spooky basement of the spooky house.  You do not like spooky basements. There are doorways to the west and east")
    if location == "West Basement" and flashlight_on == False:
        print ("It is very dark in here. You are likely to be eaten by a grue.")
    if location == "West Basement" and flashlight_on == True:
        print ("There is a desk with drawers in here. This is a really boring basement. There is a doorway to the east.")
    if location == "East Basement" and flashlight_on == True:
        print ("There is a glass box in the corner.  It looks to have something inside it. There is a doorway to the west.")
    if location == "East Basement" and flashlight_on == False:
        print ("You cannot see anything. You should turn back before you trip over something, or someone.")
    if location == "Inside House" and entered == True:
        print ("There is a person inside the house.  He seems very spooky.")
        print ("The spooky person says 'Welcome to the spooky house!  There are no pumpkin people here.'")
        print ("'We must cure the pumpkin people. I know that there is a machine on the 3rd floor to do it but the doors upwards are locked.'")
        print ("'The first key is in there', they say as they point towards a door to the north of you.")
        entered = False
    elif location == "Inside House":
        print("You are back in a barren room with a man flipping a coin in the corner")
    if location == "Kitchen" and candles_on == False:
        print("You cautiously walk into the kitchen, a messy room with things strewn all about but it all comes together for the centerpiece: An alter littered with candles throughout")
        print("The bulk of the clutter is on the floor.")
    elif location == "Kitchen":
        print("This is a very messy room with an alter that is alight and seems to have been activated.")
    if location == "Kitchen" and door_open == True:
        print("There are stairs leading to an unlocked door.")
    elif location == "Kitchen":
        print("There are stairs leading to a locked door.")
    if location == "Living Room" and door1_open == True:
        print("This room contains a table with a screwdriver on it, a crate, and a statue with a key around it's neck.  The kitchen is below you.")
    global crate_open
    if crate_open == True:
        global rope_taken
        if rope_taken == False:
            print("The crate is open and there is a rope inside.")
        else:
            print("The crate is open but empty.")
    elif location == "Living Room" and door1_open == False:
        print ("This door is locked.")
    if location == "Attic":
        print ("This room has a patch of dirt on the floor.  Spooky!")
        print ("The living room is below you.")
    if safe_open == True:
        print("There is also a safe that is open here. There are pumpkin seeds inside")
    elif location == "Attic" and door2_open == False:
        print ("This door is locked.")

def west(location):
    if (location == "South of House"):
        location = "West of House"
        look("West of House", flashlight_on)
    elif (location == "North of House"):
        location = "West of House"
        look("West of House", flashlight_on)
    elif (location == "Main Basement"):
        location = "West Basement"
        look("West Basement", flashlight_on)
    elif (location == "East Basement"):
        location = "Main Basement"
        look("Main Basement", flashlight_on)
    else:
        print("You cannot move that direction")
    return location

def east(location): 
    if (location == "North of House"):
        location = "East of House"
        look("East of House", flashlight_on)
    elif (location == "South of House"):
        location = "East of House"
        look("East of House", flashlight_on)
    elif (location == "Main Basement"):
        location = "East Basement"
        look("East Basement", flashlight_on)
    elif (location == "West Basement"):
        location = "Main Basement"
        look("Main Basement", flashlight_on)
    else:
        print("You cannot move that direction", flashlight_on)
    return location

def south(location):
    if (location == "West of House"):
        location = "South of House"
        look("South of House", flashlight_on)
    elif (location == "East of House"):
        location = "South of House"
        look("South of House", flashlight_on)
    elif (location == "Kitchen"):
        location = "Inside House"
        look("South of House", flashlight_on)
    else:
        print("You cannot move that direction")
    return location

def north(location):
    global door_open
    if (location == "West of House"):
        location = "North of House"
        look("North of House", flashlight_on)
    elif (location == "East of House"):
        location = "North of House"
        look("North of House", flashlight_on)
    elif (location == "South of House" and door_open == True):
        location = "Inside House"
        look("Inside House", flashlight_on)
    elif (location == "Inside House"):
        location = "Kithcen"
        look("Kitchen", flashlight_on)
    else:
        print("You cannot move that direction")
    return location

def up(location):
    if (location == "Main Basement"):
        location = "North of House"
        look("North of House", flashlight_on)
    elif (location == "Kitchen"):
        location = "Living Room"
        look("Living Room", flashlight_on)
    elif (location == "Living Room"):
        location = "Attic"
        look("Attic", flashlight_on)
    else:
        print("You cannot move that direction")
    return location

def down(location):
    if location == "North of House":
        location = "Main Basement"
        look("Main Basement", flashlight_on)
    elif location == "Attic":
        location = "Living Room"
        look("Living Room", flashlight_on)
    elif location == "Living Room":
        location = "Kitchen"
        look("Kitchen", flashlight_on)
    else:
        print("You cannot move that direction")
    return location

def hit(object, subject):
    if (object == "hammer" and subject == "box"):
        print ("You strike the glass box with the hammer, and it shatters.")
        print ("In the shards of broken glass lies a key")
        global box_smashed
        box_smashed = True
    elif (object == "hammer" and subject == "window"):
        print ("You hit the window with the hammer, and it bounces off the glass and hit you in the head.")
        print ("You cannot smash open the window, sorry.")
    elif object == "hammer":
        print ("You cannot hit this object with your hammer")
    else:
        print("You cannot hit things with that")

def examine(object, location):
    global safe_open
    if (object == "door" and location == "North of House"):
        print("The door is a boring wooden door with a silver handle and seems to be open")
    elif (object == "window" and location == "South of House"):
        print("The windows are sealed.  You cannot see inside them as they are covered in cobwebs.")
    elif (object == "glass box" and location == "East Basement"):
        print("There seems to be something inside the box, but you cannot see a way to open it.")
    elif (object == "door" and location == "South of House"):
        print("The door is locked shut.")
    elif (object == "desk" and hammer_taken == False):
        print("Inside the top drawer you find a hammer.")
    elif (object == "mailbox" and mailbox_open == True and flashlight_taken == False):
        print("Inside you find a small flashlight covered in dust")
    elif (object == "mailbox" and mailbox_open == True):
        print ("The mailbox is empty except for a lot of dust")
    elif (object == "floor" and location == "Kitchen"):
        print("Covering the entire floor you see pumpkin rinds, a matchbox, a few stray nails, old soda cans, and a ball of yarn")
    elif (object == "altar" and candles_on == False):
        print ("The ornate altar is painted with disturbing images of the pumpkin people. You notice some candles set in the middle of the altar.")
    elif (object == "altar" and candles_on == True):
        print ("You see the ornate altar, glowing with light from the lit candles")
    elif (object == "crate" and crate_open == True):
        print ("The only thing inside the crate is a long bundle of rope.")
    elif (object == "crate" and crate_open == False):
        print ("The crate is sealed by four screws.")
    elif object == "paper":
        print("6Z74")
        print("19")
    elif object == "safe" and safe_open == False:
        print("The safe requires a 4 digit code to enter. It takes letters and numbers. To input a guess just type it in.")
    elif object == "safe":
        print("The safe is open and inside lie some seeds.")
    else:
        print("There is nothing of interest to this entity or you cannot see that thing")
        
def unlock(object, door, location):
    global key_taken
    global key1_taken
    global key2_taken
    if (object == "key" and door == "door" and location == "South of House" and key_taken == True):
        print ("You unlock the door and can now enter the spooky house.")
        global door_open
        door_open = True
    elif (door == "basement" and location == "North of House"):
        print ("The basement door is already unlocked and just needs to be opened.")
    elif (object == "key" and door == "door" and location == "Kitchen" and key1_taken == True):
        print("The door swings opens and you can now go up the stairs into the second floor.")
        global door1_open
        door1_open = True
    elif (object == "key" and door == "door" and location == "Living Room" and key2_taken == True):
        print ("The door creaks open and now you can go up the stairs into the third floor.")
        global door2_open
        door2_open = True
    else:
        print("You cannot open the " + door + " with a " + object + ".")

def turn_on(object):
    if object == "flashlight" and flashlight_taken == True:
        print("The flashlight is on and a beam of light that is inexplicably big for the flashlight's size comes out")
        global flashlight_on
        flashlight_on = True
        global location_global
        look(location_global, flashlight_on)
    else:
        ("Why would you try to turn that on")

def take(object, location):
    global box_smashed
    global statue_fallen
    if (object == "flashlight" and location == "South of House" and flashlight_taken == False):
        print ("Taken")
        inventory.append("flashlight")
        flashlight_taken = True
        return object
    elif (object == "hammer" and  location == "West Basement" and hammer_taken == False):
        print ("Taken")
        hammer_taken = True
        inventory.append("hammer")
        return object
    elif (object == "key" and location == "East Basement" and box_smashed == True and key_taken == False):
        print ("Taken")
        key_taken = True
        inventory.append("Key 1")
        return object
    elif (object == "nail" and location == "Kitchen" and nails_taken == False):
        print("Taken")
        nails_taken = True
        inventory.append("nails")
        return object
    elif (object == "yarn" and location == "Kitchen" and yarn_taken == False):
        print("Taken")
        yarn_taken = True
        inventory.append("yarn")
        return object
    elif (object == "matchbox" and location == "Kitchen" and matchbox_taken == False):
        print("Taken")
        matchbox_taken = True
        inventory.append("matchbox")
        return object
    elif (object == "can" and location == "Kitchen" and can_taken == False):
        print("Taken")
        can_taken = True
        inventory.append("can")
        return object
    elif (object == "key" and location == "Kitchen" and candles_on == True and key1_taken == False):
        print("Taken")
        key1_taken = True
        inventory.append("Key 1")
        return object
    elif (object == "key" and location == "Living Room" and statue_fallen == True and key2_taken == False):
       print ("Taken")
       key2_taken = True
       inventory.append("Key 2")
       return object
    elif (object == "screwdriver" and location == "Living Room" and screwdriver_taken == False):
       print ("Taken")
       screwdriver_taken = True
       inventory.append("screwdriver")
       return object
    elif (object == "rope" and location == "Living Room" and crate_open == True and rope_taken == False):
       print ("Taken")
       rope_taken = True
       inventory.append("rope")
       return object
    elif object == "seed" and location == "Attic" and safe_open == True and seeds_taken == False:
        seeds_taken = True
        inventory.append("pumpkin seeds")
        print("Taken")
    else:
        print ("You cannot pick up this object because it is unimportant and making the code for you to pick it up would be a waste of time.")
def open(object, key):
    global location_global
    if (object == "mailbox"):
        print ("You open the mailbox")
    elif (object == "window"):
        print ("The windows are sealed shut and cannot be opened from the outside")
    elif (object == "door" and location_global == "North of House"):
        global basement_open
        basement_open = True
        print("The door opens easily")
    elif (object == "crate" and key == "screwdriver"):
        print("The top comes off and a long rope with a loop at the end is revealed.")
        global crate_open
        crate_open = True
    else:
        print ("This cannot be opened")

def light(object, subject):
    if object == "match" and subject == "matchbox":
        print("The match lights on fire and you feel and urge to burn the house to the ground. Unfortunately you can't do that.")
        global match_on
        match_on = True
    if object == "candle" and subject == "match":
        print("The candles lights, an eerie glow emmiting from it. A key appears in the center of the alter.")
        global candles_on
        candles_on = True

def push(object):
    if object == "statue":
        print("You try to push the statue over but it it just wobble a little bit. You need to get more leverage.")
    else:
        print("Why would you try to push that")

def pull(object, puller):
    global rope_taken
    if object == "statue" and puller == "rope" and rope_taken == True:
        print("After what seems like an eternity the statue falls over and you can take the key.")
        global statue_fallen
        statue_fallen = True
"""
def open(door, location):
    if (door == "front door" and location == "South of House"):
        if door_open == True:
            print ("The front door swings open.")
        if door_open == False:
            print ("You cannot open the front door yet, it is still locked.")
        elif (door == "basement door" and location == "North of House"):
            print ("The basement door slowly creaks open, and you can see a staircase descending into the darkness.")
            print ("You can explore the basement, but since the door has no lock you still need to get inside the house to hide from the pumpkin people.")
"""
"""
def enter (door, location):
    if (location == "South of House" and door_open == True):
        print ("You enter the house.")
        location == "Inside House"
    elif (door == "basement door" and location == "North of House"):
        print ("Try going down the stairs")
    else:
        print ("You cannot enter into that.")
"""
seed_planted = False
waited = 0
import random
won = False
while won == False:
    user_input = input(">").lower()
    word_list = user_input.split()
    if user_input == "plant seed" and seeds_taken == True:
        print("You plant the seed.")
        print("All you can do it wait now I guess.")
        seed_planted = True
    if seed_planted == True and location_global == "Attic" and user_input == "wait":
        randint = random.randint(1, 6)
        if waited == 19:
            print("The plant has finally fully grown! A green gas floats away from it.")
            print("You rush to the window and see the pumpkin people that surrounded the house were being cured by the gas.")
            print("You win!")
            won = True
        elif randint == 1:
            print("You are waiting!")
        elif randint == 2:
            print("The plant seems to be growing but you can't be sure.")
        elif randint == 3:
            print("You begin to nod off put you remember that you have to cure the pumpkin people!")
        elif randint == 4:
            print("Are you sure this is even going to work?")
        elif randint == 5:
            print("You know you look very stupid sitting there twiddling your thumbs.")
        elif randint == 6:
            print("You got this!")
        waited += 1
    if user_input == "6z74" and location_global == "Attic":
        safe_open = True
        print("The safe opens. Finally!")
    if user_input == "look":
        l = location_global
        look(l, flashlight_on)
    if user_input == "west" or user_input == "w":
        l = location_global
        location_global = west(l)
    if user_input == "east" or user_input == "e":
        l = location_global
        location_global = east(l)
    if user_input == "south" or user_input == "s":
        l = location_global
        location_global = south(l)
    if user_input == "north" or user_input == "n":
        l = location_global
        location_global = north(l)
    if user_input == "up" or user_input == "u":
        l = location_global
        location_global = up(l)
    if user_input == "down" or user_input == "d":
        l = location_global
        location_global = down(l)
    if len(word_list) == 4:
        if word_list[0] == "hit" and word_list[2] == "with":
            hit(word_list[3], word_list[1])
        if word_list[0] == "unlock" and word_list[2] == "with":
            unlock(word_list[3], word_list[1], location_global)
        if word_list[0] == "light" and word_list[2] == "with":
            light(word_list[1], word_list[3])
        if word_list[0] == "open" and word_list[2] == "with":
            open(word_list[1], word_list[3])
        if word_list[0] == "pull":
            pull(word_list[1], word_list[3])
    elif word_list[0] == "hit":
        print("To hit something enter 'hit' - 'object' - 'with' - 'subject'")
    elif word_list[0] == "unlock":
        print("To unlocks something input 'unlock' - 'door' - with 'item'")
    elif word_list[0] == "light":
        print("To light someone input 'light' - object - 'with' - subject")
    elif word_list[0] == "pull":
        print("To pull something input 'pull' - object - 'with' - subject")
    #if user_input == "enter":
    #    l = location_global
    #    location_global = enter(l)
    elif len(word_list) == 2:
        if word_list[0] == "examine":
            examine(word_list[1], location_global)
        if word_list[0] == "open":
            open(word_list[1], '')
            if word_list[1] == "mailbox":
                mailbox_open = True
        if word_list[0] == "take":
            take(word_list[1], location_global)
    elif word_list[0] == "examine":
        print("To examine something input 'examine' - 'object'")
    elif word_list[0] == "open":
        print("To attempt to open something input 'open' - 'object'")
    elif word_list == "open":
        print("To attempt to take an item input 'take' - 'object'")
    if user_input == "inventory":
        for i in range(len(inventory)):
            print(inventory[i])
    if len(word_list) == 3:
        if word_list[0] == "turn" and word_list[1] == "on":
            turn_on(word_list)
