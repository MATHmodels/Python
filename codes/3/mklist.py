def mklist(start, stop, step=1):
    result = []
    value = start
    while value <= stop:
        result.append(value)
        value += step
    return result

mylist = mklist(2, 5, 0.5)
print('mklist(2, 5, 0.5) =', mylist)
