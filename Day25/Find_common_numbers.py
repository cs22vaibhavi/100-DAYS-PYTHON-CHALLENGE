def find_common(list1, list2):
    common = []

    for number in list1:
        if number in list2:
            common.append(number)

    return common


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print("Common numbers =", find_common(list1, list2))
