"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    median = 0
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers = sorted(numbers) #sort list
        if (len(numbers) % 2 == 0):
            median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) /2 #add the two elements next to each other when halfing the list and then half the value to work out the median
        else:
            median = numbers[len(numbers)//2] #half list immediately for an odd number of elements in a list

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break


print(median)
