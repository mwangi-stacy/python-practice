#Allow the user to enter a list of numbers, with no specified limit
numbers =input("Enter numbers with spaces in between:")


#Creating the function to sum up all those numbers
def sum_elements():
    #To split the numbers into individual strings
    numbers_list = numbers.split(" ")

    #To convert the split numbers into integers for addition
    number = [int(num) for num in numbers_list]

    #To add the elements together
    total_sum = sum(number)

    #To print out the result
    print("The total sum for the numbers you gave is:", total_sum)

# Call the function
sum_elements()




