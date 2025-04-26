number = int(input("Please enter a positive integer (0 or greater): "))

def calculate_fact_recursive(number):
    # To print the factorial of 0 separately
    if number == 0 or number == 1:
        return  1
    #Recursive case to call the function in itself to get the factorial
    else:
        return number * calculate_fact_recursive(number - 1)

print(calculate_fact_recursive(number))
