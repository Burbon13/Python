from utils.area import find_points


def bktF(points, pos, bk):
    if pos >= 4:
        if find_points(points, pos - 1, bk):
            for i in range(1, pos):
                print(points[bk[i] - 1], end=' ')
            print()

    '''
    for i in range(1, pos):
        print(bk[i], end=' ')
    print()
    '''

    if pos <= len(points):
        for i in range(bk[pos-1] + 1, len(points) + 1):
            bk[pos] = i
            bktF(points, pos + 1, bk)

def bktRec(points):
    bk = [0] * (len(points) + 2)
    bktF(points, 1, bk)
