"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
numbers.sort()
if (numbers.len() == 0):
    print("Empty list so no median.")
    return 0
elif (numbers.len() == 1):
    return numbers[0]
else:
    if (numbers.len()%2 == 0):
        median = (numbers[(numbers.len()/2)] + numbers[(numbers.len()/2)+1]) /2
        return median
    else:
        medianvalue = numbers[(numbers.len()+1) / 2]
        return medianvalue
