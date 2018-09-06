def area(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) + (p1[0] - p3[0]) * (p2[1] - p1[1])


def find_points(points, pos, bk):
    for i1 in range(1, pos + 1):
        for i2 in range(i1 + 1, pos + 1):
            for i3 in range(i2 + 1, pos + 1):
                if area(points[bk[i1] - 1], points[bk[i2] - 1], points[bk[i3] - 1]) == 0:
                    print(points[bk[i1] - 1], end=",")
                    print(points[bk[i2] - 1], end=",")
                    print(points[bk[i3] - 1], end=" : ")
                    return True
    return False
