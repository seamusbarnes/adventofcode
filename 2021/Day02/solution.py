import numpy as np
from functools import wraps
import time

def main():

    def timeit(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t0 = time.time()
            result = func(*args, *kwargs)
            t1 = time.time()
            print(f'\n{func.__name__} completed in {(t1-t0):.2f} s\n')
            return result
        return wrapper
    
    @timeit
    def load_data(filename=None):

        if filename == None:
            filename = 'input.txt'
        
        with open(filename, 'r') as file:
            data = [((line.split(' '))[0], int(line.split(' ')[1])) for line in file.read().splitlines()]
        return data
    
    def calc_position(data):
        hor, dep, aim = 0, 0, 0
        for i in range(len(data)):
            command, value = data[i][0], data[i][1]

            if command == 'forward':
                hor += value
                dep += aim*value

            elif command == 'down':
                # dep += value
                aim += value
            elif command == 'up':
                # dep -= value
                aim -= value
        
        return hor, dep, aim
    
    # data = load_data('dummy_input.txt')
    data = load_data()

    (hor, dep, aim) = calc_position(data)
    
    print(f'Horizontal position: {hor}')
    print(f'Depth position: {dep}')
    print(f'Horizontal x depth: {hor*dep}')

    print(f'Aim: {aim}')

if __name__ == '__main__':
    main()