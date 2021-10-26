import math
import matplotlib.pyplot as plt

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
#           41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
primes = [2, 3, 5]


def is_factorable_by_primes(number):
    for prime in primes:
        while number % prime == 0:
            number = number / prime
    return number == 1


all_numbers = range(1, 1000)
factorable_numbers = []


def plot3(x):
    limit = math.log(x, 3) + 1
    return math.log(x, 2) * limit - math.log(3, 2) * limit * (limit - 1) / 2


def plot5(x):
    value = 0
    for i in range(50):
        for j in range(50):
            value += max(math.log(x / 3**i / 5**j, 2), 0)
    return value


def plot5_formula(x):
    return sum([
        sum([
            math.log(x / 3**i / 5**j, 2)
            for j in range(math.floor(math.log(x, 5)) + 1)
        ])
        for i in range(math.floor(math.log(x, 3)) + 1)
    ])


def plot5_2(x):
    value = 0
    for i in range(50):
        for j in range(50):
            value += max((1 if i % 3 == 0 else 0) +
                         math.log(x / 3**i / 5**j, 2), 0)
    return value


for i in all_numbers:
    if i < 2:
        factorable_numbers.append(0)
        continue

    if is_factorable_by_primes(i):
        factorable_numbers.append(factorable_numbers[-1] + 1)
    else:
        factorable_numbers.append(factorable_numbers[-1])

plt.plot(all_numbers, factorable_numbers, "b",
         #  all_numbers, [sum([max(1+math.log(i/3**j, 2), 0)
         #                     for j in range(100)]) for i in all_numbers], "r",
         #  all_numbers, [sum([max(0+math.log(i/3**j, 2), 0)
         #                     for j in range(100)]) for i in all_numbers], "g",
         #  all_numbers, [sum([max((1 if j % 3 == 0 else 0)+math.log(i/3**j, 2), 0)
         #                     for j in range(100)]) for i in all_numbers], "r",
         all_numbers, [plot5(i) for i in all_numbers], "y",
         all_numbers, [plot5_2(i) for i in all_numbers], "r",
         all_numbers, [plot5_formula(i) for i in all_numbers], "g")
plt.show()
