# Let the user input the number they would like to calculate its factorial
number = int(input("Enter the factorial you wish to calculate: "))

# To ensure the user inputs only positive integers
while number < 0:
    print("Sorry, negative numbers have no factorial.")
    number = int(input("Please enter a positive integer (0 or greater): "))

# Function to calculate the factorial
def calculate_factorial(number):
    # Initialize factorial as one since the first factorial, which is that of zero is 1
    factorial = 1
    #For loop for carrying out the factorial calculation
    for i in range(1, number + 1):
        factorial= factorial * i

    # To print out the final result
    print("The factorial of {} is {}".format(number, factorial))

# To print the factorial of 0 separately
if number == 0:
    factorial=1
    print("The factorial of {} is {}.".format(number, factorial))
else:
    # Calling the function
    calculate_factorial(number)
