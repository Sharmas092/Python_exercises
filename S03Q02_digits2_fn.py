""" What does this program do ?
"""

# Implement the helper functions here
def do_1digit_oper(number):
    new_value = number+7
    units_place = new_value % 10
    print("Number in unit's place", units_place )
    return units_place
def do_2digit_oper(number):
    new_value = number**5
    units_place = new_value % 10
    print("Number in unit's place", units_place )
    return units_place
def do_3digit_oper(number):
    new_num = int(input("Please enter another number: " ))
    new_value = new_num + 2
    units_place = new_value % 10
    print("Number in unit's place", units_place )
    return units_place
        
def perform_check():
    """ This function prompts the user for a number
            It returns an integer [ and not a string ]
    """
    number = int(input("Please enter the number: "))   
    if 0 <= number <= 10:
        do_1digit_oper(number)
    elif 10 <= number <= 99:
        do_2digit_oper(number)
    elif 100 <= number <= 999:
        do_3digit_oper(number)
    else:
        print("The number has more than 3 digits or is not supported.")    
        
# Main starts from here
perform_check()
