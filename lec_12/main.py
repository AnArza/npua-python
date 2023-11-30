import random

from utils import read_file_generator, execution_time

filename = 'random_numbers.txt'

with open(filename, 'w') as file:
    for _ in range(100):
        numbers = [str(random.randint(1, 1000)) for _ in range(20)]
        file.write(' '.join(numbers) + '\n')

filtered_numbers_arrays = []
with open(filename, 'r') as file:
    for line in file:
        integer_array = list(map(int, line.split()))
        filtered_numbers_arrays.append(list(filter(lambda x: x > 40, integer_array)))

with open(filename, 'w') as file:
    for numbers in filtered_numbers_arrays:
        file.write(' '.join(map(str, numbers)) + '\n')


@execution_time
def process_file(file_path):
    for line in read_file_generator(file_path):
        print(line)


process_file(filename)
