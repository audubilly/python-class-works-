billy_list = [11, 2, 4, 7, 9, 0, 11, 3, 6]


def sort_Numbers(arg: []) -> []:
    even_list = []
    odd_list = []

    arg.sort()
    for i in arg:
        if i % 2 == 0:
            even_list.append(i)

        if i % 2 != 0:
            odd_list.append(i)

    even_list += odd_list
    return even_list


print(sort_Numbers(billy_list))
