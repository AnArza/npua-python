from number_classification import classify_numbers

numbers = [int(num) for num in input('Please enter a list of numbers separated by spaces: ').split()]

classified_numbers = classify_numbers(numbers)

print(f'Even numbers are: {classified_numbers[0]}')
print(f'Odd numbers are: {classified_numbers[1]}')
