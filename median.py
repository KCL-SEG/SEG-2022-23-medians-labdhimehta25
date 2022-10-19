"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        median = 0
        numbers.sort()
        if (numbers.len() == 1):
            return numbers[0]
        else:
            if (numbers.len()%2 == 0):
                median = (numbers[(numbers.len()//2) - 1] + numbers[(numbers.len()//2)+1]) /2
            else:
                median = numbers[(numbers.len())// 2]

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break


print(median)
