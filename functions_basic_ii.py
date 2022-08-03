# 1 -- Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(number):
    list = []
    for i in range(number, 0, -1):
        list.append(i)
    return list

# Vlaidation
x = countdown(10)
print(x)

# 2 -- Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(list):
    print(list[0])
    return list[1]

# Validation
print(print_and_return([20,3]))

# 3 -- First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(list):
    return list[0] + len(list)

# Validation
print(first_plus_length([2,4,6,3,1]))

# 4 -- Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def greater_than_second(list):
    newList = []
    for i in list:
        if i > list[1]:
            newList.append(i)
    print(len(newList))
    return newList

# Validation
greater_than_second([3,2,6,7,2,9,5,6,3,9,5,6,0])

# 5 -- This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_value(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list

#Validation
print(length_value(3,7))


