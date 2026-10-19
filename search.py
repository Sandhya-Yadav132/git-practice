def add(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add(4,5,5))