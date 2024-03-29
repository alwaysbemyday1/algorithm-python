# 행렬 제곱
def square_matrix():
    import sys
    input = sys.stdin.readline
    
    N, B = map(int, input().split())
    A = [[*map(int, input().split())] for _ in range(N)]
    
    def mul(U, V):
        n = len(U)
        Z = [[0]*n for _ in range(n)]
        
        for row in range(n):
            for col in range(n):
                e = 0
                for i in range(n):
                    e += U[row][i] * V[i][col]
                Z[row][col] = e % 1000
    
        return Z
    
    def square(A, B):
        if B == 1:
            for x in range(len(A)):
                for y in range(len(A)):
                    A[x][y] %= 1000
            return A
        
        tmp = square(A, B//2)
        if B % 2:
            return mul(mul(tmp, tmp), A)
        else:
            return mul(tmp, tmp)
    
    result = square(A, B)
    for r in result:
        print(*r)


# 행렬 곱셈
def multiple_matrix():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    M, K = map(int, input().split())
    B = []
    for _ in range(M):
        B.append(list(map(int, input().split())))

    C = [[0 for _ in range(K) for _ in range(N)]]

    for n in range(N):
        for k in range(K):
            for m in range(M):
                C[n][k] += A[n][m] * B[m][k]

    for i in C:
        for j in i:
            print(j, end=' ')
        print()


# 이항 계수 3
def binomial_coefficient_3():

    def power(a, b):
        if b == 0:
            return 1
        if b % 2:
            return (power(a, b // 2)**2 * a) % p
        else:
            return (power(a, b // 2)**2) % p

    p = 1000000007
    N, K = map(int, input().split())
    fact = [1 for _ in range(N + 1)]

    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i % p

    A = fact[N]
    B = (fact[N - K] * fact[K]) % p

    print((A % p) * (power(B, p - 2) % p) % p)


# 곱셈
def multiple_dnc_vers2():
    a, b, c = map(int, input().split())

    def dnc(a, b, c):
        if b == 1:
            return a % c
        elif b % 2 == 0:
            return (dnc(a, b // 2, c)**2) % c
        else:
            return ((dnc(a, b // 2, c)**2) * a) % c

    print(dnc(a, b, c))


# RecursionError
def multiple_dnc_vers1():
    a, b, c = map(int, input().split())

    def rcrs(a, aa, time, div):
        if time == 0:
            print(aa)
            return
        rcrs(a, a * aa % div, time - 1, div)

    rcrs(a, 1, b, c)


# 종이의 개수
def num_of_paper():
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]

    rl = [0, 0, 0]

    def rcrs(x, y, N):
        start = paper[x][y]
        for i in range(x, x + N):
            for j in range(y, y + N):
                if paper[i][j] != start:
                    N //= 3
                    for k in range(3):
                        for l in range(3):
                            rcrs(x + k * N, y + l * N, N)
                    return
        rl[start] += 1

    rcrs(0, 0, N)
    print(rl[-1])
    print(rl[0])
    print(rl[1])
