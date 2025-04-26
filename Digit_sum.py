#Prompt the user to enter a number of choice
number = int(input("Please enter a number: "))

#Define the function to calculate the sum of digits
def digit_sum(number):
    #For if the number entered is 0
    if number == 0:
        return 0
    else:
        total_sum = 0
        #For loop that converts the number entered to a string , and identifies the digits as individual characters
        for digit in str(number):
            #Convert the individual digit characters back to
            total_sum += int(digit)
        return total_sum

    # Call the function and print the result
result = digit_sum(number)
print("The sum of the digits is:", result)

