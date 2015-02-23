def product_of_other_nums(num_lst):
    result = [1] * len(num_lst)

    current_product = 1
    for i in range(len(num_lst)):
        result[i] *= current_product
        current_product *= num_lst[i]

    current_product = 1
    for i in range(len(num_lst), 0, -1):
        result[i - 1] *= current_product
        current_product *= num_lst[i - 1]

    return result


def highest_product_of_three(num_lst):
    highest = max(num_lst[0], num_lst[1])
    lowest = min(num_lst[0], num_lst[1])
    
    highest_of_two = num_lst[0] * num_lst[1]
    lowest_of_two = num_lst[0] * num_lst[1]
    highest_of_three = num_lst[0] * num_lst[1] * num_lst[2]

    for num in num_lst[2:]:
        if num * highest_of_two > highest_of_three:
            highest_of_three = num * highest_of_two

        if num * highest > highest_of_two:
            highest_of_two = num * highest

        if num > highest:
            highest == num

        if num * lowest_of_two > highest_of_three:
            highest_of_three = num * lowest_of_two

        if num * lowest < lowest_of_two:
            lowest_of_two = num * lowest

        if num < lowest:
            lowest = num

        print highest, highest_of_two, highest_of_three, lowest, lowest_of_two

    return highest_of_three