

def cut_rod(p, n):
    if n == 0:
        return 0

    r = {0: 0}
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            q = max(q, p[i]+cut_rod(p, j-i))
        r[j] = q
    return r[n]


if __name__ == "__main__":
    nPrices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    length = 3
    revenue = cut_rod(nPrices, length)
    print(revenue)
