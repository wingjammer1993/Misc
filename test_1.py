A = [1, 2, 3, 4, 24, 1]


def findSpike(A, s, t):

        check = (s + t) // 2
        elem = A[check]

        if check != 0 and A[check-1] < elem and A[check+1] < elem:
            return elem

        elif (A[check-1] < elem and A[check+1] > elem) or check == 0:
            return findSpike(A, check+1, t)

        else:
            return findSpike(A, s, check-1)


answer = findSpike(A, 0, len(A)-1)
print(answer)