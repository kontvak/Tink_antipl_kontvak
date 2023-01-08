def rast(a, b):
    def recurs(i, j):
        if i == 0:
            return j
        elif j == 0:
            return i
        elif a[i-1] == b[j-1]:
            return recurs(i - 1, j - 1)
        else:
            return 1 + min(recurs(i, j - 1),
                           recurs(i - 1, j),
                           recurs(i - 1, j - 1)
                           )
    return recurs(len(a), len(b))

print(rast('sdadhasjd', 'sdfsdsdfsfd'))