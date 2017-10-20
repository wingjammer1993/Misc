
def fib(n):
    f_num = {0: 0, 1: 1}
    for i in range(2, n+1):
        f_num[i] = f_num[i-1] + f_num[i-2]
    return f_num[n]


if __name__ == "__main__":
    num = fib(4)
    print(num)