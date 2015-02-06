def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst)/2
    lst_a = merge_sort(lst[0:mid])
    lst_b = merge_sort(lst[mid:])

    sorted_list = []

    while len(lst_a) > 0 and len(lst_b) > 0:
        if lst_a[0] > lst_b[0]:
            sorted_list.append(lst_b.pop(0))
        else:
            sorted_list.append(lst_a.pop(0))

    sorted_list.extend(lst_a)
    sorted_list.extend(lst_b)

    return sorted_list


def bubble_sort(lst):
    pass




def main():
    pass

if __name__ == "__main__":
    main()