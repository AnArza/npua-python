import time


def read_file_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'The function executed in {end_time - start_time} seconds')
        return res
    return wrapper
