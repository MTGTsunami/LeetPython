def insertion_sort(l):
    for i, x in enumerate(l[1:]):
        key = x
        j = i
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key


a = [4, 1, 7, 5, 9, 2, 6, 8, 0]
print(a)
insertion_sort(a)
print(a)
