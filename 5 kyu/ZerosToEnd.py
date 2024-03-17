def move_zeros(lst):
    for n in lst:
        if n == 0:
            lst.append(lst.pop(lst.index(n)))
    return lst