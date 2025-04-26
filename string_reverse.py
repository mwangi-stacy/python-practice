# Allow the user to input a word or a string of words
my_string = input("Please enter a word or string of words: ")

# Defining a function that reverses the output
def reverse_string(my_string):
#Initialise a variable that will hold the reverse of the input
    reversed_string = ""
#Using a for loop that will pick each character, and complete the reversing process by adding the last character to the initial character(prepending)
    for char in my_string:
        reversed_string = char + reversed_string
    return reversed_string


#To call the function out and print out the final product
final_string = reverse_string(my_string)
print("Your input in reverse is:", final_string)