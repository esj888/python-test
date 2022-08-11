# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


print(my_sum(1, 2, 3))


# concatenate_keys.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the keys of the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result


print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

