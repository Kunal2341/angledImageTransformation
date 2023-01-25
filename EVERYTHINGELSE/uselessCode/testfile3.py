def find_close_values(lst, threshold):
    """
    Find all values in list that are close to each other
    """
    lst.sort()
    close_values = []
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] >= threshold:
            close_values.append(lst[i])
    return close_values

a = [0, 1, 2, 3, 4, 6, 8, 10, 13, 17, 21, 26, 33, 41, 51, 63, 77, 94, 115, 141, 173, 211, 258, 315, 384, 468, 571, 696, 848, 1033, 1222, 1487, 1862, 2265]
threshold = 10
resultingListLenght = 0
while resultingListLenght !=21:
    new_list = find_close_values(a, threshold)
    resultingListLenght = len(new_list)
    if resultingListLenght != 21:
        threshold -= 1
print(new_list)
print(len(new_list))