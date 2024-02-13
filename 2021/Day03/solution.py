import numpy as np

def load_data(filename='input.txt'):

    with open(filename, 'r') as file:
        data = [line for line in file.read().splitlines()]

    return data

def calc_mode_bits(data):
    n = len(data)
    store = [0] * len(data[0])

    n_store = len(store)
    for i in range(n):
        for j in range(n_store):
            store[j] += int(data[i][j])

    for i in range(n_store):
        if store[i] > n/2:
            store[i] = 1
        else:
            store[i] = 0

    return store

def calc_least_common_bits(mode_bits):
    res = []
    for i in range(len(mode_bits)):
        if mode_bits[i] == 1:
            res.append(0)
        else:
            res.append(1)
    return res

def calc_gamma(mode_bits):
    gamma = 0
    power = 0
    for i in range(len(mode_bits)-1, -1, -1):
        gamma += (mode_bits[i] * 2**power)
        power += 1

    return gamma

# data = load_data('dummy_input.txt')
data = load_data()
mode_bits = calc_mode_bits(data)
gamma = calc_gamma(mode_bits)

least_common_bits = calc_least_common_bits(mode_bits)
print(least_common_bits)
epsilon = calc_gamma(least_common_bits)

print(gamma)
print(epsilon)

print(gamma*epsilon)