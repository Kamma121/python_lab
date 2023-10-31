def flatten(sequence):
    result_list = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result_list.extend(flatten(item))
        elif isinstance(item, int):
            result_list.append(item)
    return result_list


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(seq))
