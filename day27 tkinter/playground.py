def add(*args):
    total = 0
    for num in args:
        total += num

    return total


print(add(1, 2, 3, 4, 5))
print(add(10, 20, 30))
