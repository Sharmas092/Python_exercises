""" What does this program do ?
"""

def do_action(present, redmark, bluemark):
    # Compare present with redmark and bluemark
    # to decide the appropriate action
    if present > redmark:
        print("Warning: Level", present , " is too high! Drain the tank.")
    
    elif present < bluemark :
        print("Warning: Level", present , " is too low! Please send SMS to buy more liquid.")
    else:
        print("Level" , present, "is normal. No action required.")
        

def get_current_level():
    # Get value from user
    # Return integer
    current_level = float(input("Please enter the current level of ethanel in the tank"))
    return current_level

# Main starts from here
capacity = 900
high = capacity * 0.8
low = capacity * 0.2
level = get_current_level()
do_action(level, high, low)
