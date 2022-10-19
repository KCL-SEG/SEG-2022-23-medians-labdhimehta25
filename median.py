"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    median = 0
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers = sorted(numbers)
        if (len(numbers) % 2 == 0):
            median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2 +1] /2
        else:
            median = numbers[len(numbers)//2]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break


print(median)
