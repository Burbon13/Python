from utils.area import find_points


def bktIt(points):
    pos = 1
    bk = [0] * (len(points) + 2)

    while pos > 0:
        if bk[pos] == 0:
            bk[pos] = bk[pos-1] + 1
        else:
            bk[pos] = bk[pos] + 1

        if bk[pos] > len(points):
            bk[pos] = 0
            pos = pos - 1
            continue

        '''
        for i in range(1,pos+1):
            print(bk[i], end=' ')
        print()
        '''
        if find_points(points, pos, bk):
            for i in range(1, pos+1):
                print(points[bk[i] - 1], end=' ')
            print()

        pos = pos + 1