"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    median = 0
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers = sorted(numbers)
        if (numbers.len()%2 == 0):
            median = (numbers[(numbers.len()//2) - 1] + numbers[(numbers.len()//2)+1]) /2
        else:
            median = numbers[(numbers.len())// 2]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break


print(median)
