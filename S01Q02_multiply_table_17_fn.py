""" 
To print 17th table using function
"""

def print_mtable():
    """ 
        Describe what this function does
    """
    # Your solution code goes in here
    num1 = 17
    for num2 in range (1, 11):
        result = num1 * num2
        print(num1, '*', num2, '=', result)

# Main starts from here
print_mtable()
