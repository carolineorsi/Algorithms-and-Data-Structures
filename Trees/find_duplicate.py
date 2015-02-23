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


def find_duplicate_nondestructive(lst):
    min = 1
    max = len(lst) - 1

    while min < max:
        mid = min + ((max - min) / 2)
        low_min, low_max = min, mid
        high_min, high_max = mid + 1, max

        count = 0
        for num in lst:
            if num >= low_min and num <= low_max:
                count += 1

        if count > low_max - low_min + 1:
            max = low_max
        else:
            min = high_min

    return min




###########################################################################################

if __name__ == "__main__":
    pass