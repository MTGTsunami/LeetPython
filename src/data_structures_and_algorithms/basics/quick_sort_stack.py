l = [2, 4, 6, 3, 8, 1, 9, 7, 13]


def get_index(l, low, high):
    temp = l[low]

    while low < high:
        while l[high] >= temp and low < high:
            high -= 1
        l[low] = l[high]

        while l[low] <= temp and low < high:
            low += 1
        l[high] = l[low]

    index = low
    l[index] = temp

    return index


def quick_sort(l):
    stack = []
    low = 0
    high = len(l) - 1
    index = get_index(l, low, high)

    if index > low + 1:
        stack.append(low)
        stack.append(index - 1)

    if index < high - 1:
        stack.append(index + 1)
        stack.append(high)

    while len(stack) != 0:
        high = stack.pop()
        low = stack.pop()
        idx = get_index(l, low, high)

        if idx > low + 1:
            stack.append(low)
            stack.append(idx - 1)

        if idx < high - 1:
            stack.append(idx + 1)
            stack.append(high)


print(l)
quick_sort(l)
print(l)


