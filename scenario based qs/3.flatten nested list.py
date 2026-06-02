# 3. Flatten Nested List
# data = [1, [2, [3, 4], 5], 6]
# Task: Convert it into a single flattened list:
# [1, 2, 3, 4, 5, 6]

def flatten(lst):
    result = []

    for item in lst:
        if isinstance(item,list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


data = [1, [2, [3, 4], 5], 6]
print(flatten(data))


