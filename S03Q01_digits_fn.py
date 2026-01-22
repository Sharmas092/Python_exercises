""" What does this program do ?
"""

# Implement the helper functions here

def perform_check(number):
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    if 10<= number <=99:
        print("2 Digit number:", number)
    elif 100 <=number <= 999:
        print("3 Digit number:", number)
    else:
        print("Number is neither 2 digit nor 3 digit:" , number)
    return number
    
def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    num = int(input("Please enter the number: "))
    return num
# Main starts from here
num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)
