def find_duplicate(lst):
    index = lst[0]

    while lst[index] != 'X':
        current = index
        index = lst[index]
        lst[current] = 'X'

    return index


###########################################################################################

if __name__ == "__main__":
    pass