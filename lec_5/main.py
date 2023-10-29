from sum_of_elements import sum_of_elements

numbers = [int(num) for num in input('Please enter a list of numbers separated by spaces: ').split()]

exclude_negative = False
answer = input('Do you want to exclude negative numbers? Answer "yes" or "no".')
if answer == 'yes':
    exclude_negative = True
elif answer == 'no':
    exclude_negative = False

print(sum_of_elements(numbers, exclude_negative))
