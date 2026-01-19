""" 
    Mention what this program does
"""

def get_number():
    """ 
        This function should fetch a number from user
        Input : None
        Return : an integer
    """
    number = input("Enter any number:")# Write code to prompt the user for a number
    # Check out your code behaviour by commenting the line below
    number = int(number) # What happens if you dont perform this operation ? Ans: Python will take inout as string
    return number


def print_mtable(num):
    """ 
        This function prints the multiplication table of num
        Input : an integer
        Output : Display multiplication table of input integer
        Return : None
    """
    # Your solution code goes in here
    num1 = num
    for num2 in range (1, 11):
        result = num1 * num2
        print(num1, '*', num2, '=', result)

def main():
    '''
        Main program
    '''
    inp = get_number()
    print_mtable(inp)

# Main starts from here
main()
