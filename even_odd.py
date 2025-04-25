#Allow the user to enter a number
number= int(input("Enter any positive integer: "))

#To check if the inputted number is positive
while number < 0:
    print("Sorry, the number you entered is not a positive integer")
    number = int(input("Please enter a positive integer(greater than zero): "))

#Defining the function to check if number is
def odd_even_checker(number):

    #Using the modulus operator(remainder after division) to determine whether number is odd or even
    if number % 2 == 0:
        print(+number," is an even number")
    if number % 2 != 0:
        print(+number," is an odd number")

#Calling the function
odd_even_checker(number)