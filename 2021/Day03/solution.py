import numpy as np

def load_data(filename='input.txt'):

    with open(filename, 'r') as file:
        data = [line for line in file.read().splitlines()]

    return data

def calc_most_common_bits(data, bit=1):
    n = len(data)
    store = [0] * len(data[0])

    n_store = len(store)
    for i in range(n):
        for j in range(n_store):
            store[j] += int(data[i][j])

    for i in range(n_store):
        if store[i] > n/2:
            store[i] = bit
        else:
            store[i] = abs(bit-1)

    return store

def most_common_bit(data, index):
    ones = sum(int(row[index]) for row in data)
    return 1 if ones >= len(data) else 0

def calc_symbol(mode_bits):
    gamma = 0
    power = 0
    for i in range(len(mode_bits)-1, -1, -1):
        gamma += (mode_bits[i] * 2**power)
        power += 1

    return gamma

def calc_oxygen_rating(bits):
    bits_set = set(bits)
    for i in range(len(bits[0])):
        most_common_bits = calc_most_common_bits(bits)
        removals = []
        print(bits_set)
        print(most_common_bits[i])
        for key in bits_set:
            if int(key[i]) != most_common_bits[i]:
                removals.append(key)
        for rem in removals:
            bits_set.remove(rem)
    return bits_set

if __name__ == '__main__':
    print('')

    data = load_data('dummy_input.txt')
    # data = load_data()

    most_common_bits = calc_most_common_bits(data)
    gamma = calc_symbol(most_common_bits)
    print(f'Gamma: {gamma}')

    least_common_bits = calc_most_common_bits(data, 0)
    epsilon = calc_symbol(least_common_bits)
    print(f'Epsilon: {epsilon}')

    print(f'Gamma * Epsilon: {gamma*epsilon}')
    print('')

    oxygen = calc_oxygen_rating(data)
    print(oxygen)