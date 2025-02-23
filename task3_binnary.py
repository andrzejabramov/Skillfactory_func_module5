data_list = [1, 2, 3, 4]


def binary_search(data_list, find_el):
    if data_list:
        index_el = len(data_list) // 2
        if find_el > data_list[index_el]:
            return find_el in data_list[index_el+1:]
        elif find_el < data_list[index_el]:
            return find_el in data_list[:index_el]
        return True
    return False


print(binary_search(data_list, 0))