def mergeSort(l, i, j):
    if i < j:
        mid = int((i+j)/2)
        mergeSort(l, i, mid)
        mergeSort(l, mid+1, j)
        merge(l, i, mid, j)


def merge(l, first, mid, last):
    a = []
    b = []
    copy(l, first, mid, a)
    copy(l, mid+1, last, b)
    i = 0
    j = 0
    for k in range(first, last+1):
        if a[i] < b[j]:
            l[k] = a[i]
            i += 1
        else:
            l[k] = b[j]
            j += 1


def copy(l, i, j, x):
    for k in range(i, j+1):
        x.append(l[k])
    x.append(float('inf'))


l = [4, 2, 7, 5, 9, 1, 3, 6, 8]
mergeSort(l, 0, 8)
print(l)