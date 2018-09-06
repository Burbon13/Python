def gnomeSort(to_sort_list, key=lambda x: x, cmp=lambda x, y: x <= y):
    pos = 0
    while pos < len(to_sort_list):
        if pos == 0 or cmp(key(to_sort_list[pos-1]), to_sort_list[pos]):
            pos += 1
        else:
            to_sort_list[pos], to_sort_list[pos-1] = to_sort_list[pos-1], to_sort_list[pos]
            pos -= 1


def quickSort(to_sort_list, key=lambda x: x, cmp=lambda x, y: x <= y):
    if to_sort_list == []:
        return []

    pivot = to_sort_list[0]
    lesser = quickSort([x for x in to_sort_list[1:] if cmp(key(x), key(pivot))], key, cmp)
    greater = quickSort([x for x in to_sort_list[1:] if not cmp(key(x), key(pivot))], key, cmp)
    return lesser + [pivot] + greater


def sortA(to_sort_list, key=lambda x: x, cmp=lambda x, y: x <= y, reverse=False):

    #to_return = to_sort_list[:]

    #gnomeSort(to_return, key, cmp)

    to_return = quickSort(to_sort_list, key, cmp)

    if reverse:
        to_return.reverse()

    return to_return
