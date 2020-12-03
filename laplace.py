import math

# const
LIMIT = 100
N = 101  # x軸方向
M = 101  # y軸方向

# iteration() function


def iteration(u):
    u_next = [[0 for i in range(N)] for j in range(M)]

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            u_next[i][j] = (u[i][j - 1] + u[i - 1][j] +
                            u[i + 1][j] + u[i][j + 1]) / 4

    # update uij
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            u[i][j] = u_next[i][j]


# main
u = [[0 for i in range(N)] for j in range(M)]
for i in range(M):
    u[0][i] = math.sin(2 * math.pi * i / (M - 1))

for i in range(LIMIT):
    iteration(u)

print(u)
