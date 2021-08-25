import itertools
import random

min_length = 100

# '000': {'0': 0, '1': 0}, '001': {'0': 0, '1': 0}, and so on
triads = {"{}{}{}".format(*a): {'0': 0, '1': 0} for a in itertools.product(range(2), repeat=3)}


def parse():
    data = get_string()
    print('Final data string:')
    print(data)

    print('''You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!''')

    count_triads(data)

    balance = 1000
    new_str = ''
    while new_str != 'enough':
        print("Print a random string containing 0 or 1:")
        new_str = input()
        if not new_str.isnumeric():
            if new_str != 'enough':
                print('some wrong input')
            continue
        guessed_symbols = guess_str(new_str)
        if guessed_symbols > 0:
            balance -= guessed_symbols
        else:
            balance += guessed_symbols
        print("Your balance is now ${}".format(balance))
    print('Game over!')


def guess_str(new_str):
    guessed_symbols = 0
    guessed_str = ''

    for i in range(3):
        guessed_str += str(random.randint(0, 1))

    for i in range(3, len(new_str)):
        if triads[new_str[i - 3: i]]['0'] > triads[new_str[i - 3: i]]['1']:
            guessed_str += '0'
        elif triads[new_str[i - 3: i]]['0'] < triads[new_str[i - 3: i]]['1']:
            guessed_str += '1'
        else:
            guessed_str += str(random.randint(0, 1))

    for i in range(3, len(new_str)):
        if guessed_str[i] == new_str[i]:
            guessed_symbols += 1

    print('prediction:')
    print(guessed_str)
    print('Computer guessed right {0} out of {1} symbols ({2:.2f} %)'.format(guessed_symbols, len(new_str) - 3,
                                                                             ((guessed_symbols / (len(new_str) - 3)) * 100)))
    return guessed_symbols - (len(new_str) - 3 - guessed_symbols)


def count_triads(data):
    for n in range(0, len(data) - 3, 1):
        for el in triads:
            if data[n: n + 3] == el:
                if data[n + 3] == '0':
                    triads[el]['0'] += 1
                else:
                    triads[el]['1'] += 1


def print_out(data):
    for key in data:
        print('{}: {},{}'.format(key, data[key]['0'], data[key]['1']))


def get_string():
    data = ''
    while len(data) < min_length:
        print("Print a random string containing 0 or 1:")
        new_data = input()
        data = data + filter_out(new_data)
        if len(data) < min_length:
            print(f'Current data length is {len(data)}, {min_length - len(data)} symbols left')
    return data


def filter_out(data):
    ready = ''
    for num in data:
        if str(num).isnumeric():
            if int(num) == 0 or int(num) == 1:
                ready = ready + num
    return ready


parse()

