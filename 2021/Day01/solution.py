import numpy as np
import time
from functools import wraps

def main():
    
    def timeit(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t0 = time.time()
            result = func(*args, **kwargs)
            t1 = time.time()
            print(f'\n{func.__name__} took {(t1 - t0):.2f} s to execute\n')
            return result
        return wrapper
    
    @timeit
    def load_data(filename = 'input.txt'):

        with open(filename, 'r') as file:
            data = [int(line) for line in file]
    
        return data
    

    def count_increases(data):
        count = 0

        for i in range(1, len(data)):
            if (data[i] - data[i-1]) > 0:
                count += 1
        
        return count

    def sliding_window(data, ws=3):
        res = []
        for i in range(0, len(data)-ws+1):
            res.append(np.sum(data[i:i+ws]))
        
        return res

    data = load_data()
    count = count_increases(data)
    print(f'Part 01: number of increase: {count}')

    # dummy_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    data = sliding_window(data)
    count = count_increases(res)
    print(f'Part 02: number of increases: {count}')

if __name__ == '__main__':
    main()