def find_duplicate_using_index(lst):
    index = lst[0]

    while lst[index] != 'X':
        current = index
        index = lst[index]
        lst[current] = 'X'

    return index

def find_duplicate_using_sort(lst):
    lst.sort()

    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return lst[i]


###########################################################################################

if __name__ == "__main__":
    pass