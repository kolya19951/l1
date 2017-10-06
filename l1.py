# n = 4
# al = [0 for i in range(n)]
# cl = [0 for i in range(n)]
# bl = [0 for i in range(n)]
# A = [[1, 2, 0, 0], [1, 10, -5, 0, 0], [0, 1, -5, 2], [0, 0, 1, 4]]
# b = [-5, -9, -20, -27]
# alp = [0 for i in range(n)]
# bet = [0 for i in range(n)]
# x = [0 for i in range(n)]
# for i in range(0, n):
#     for j in range(0, n):
#         if (j == i - 1):
#             al[i] = A[i][j]
#         if (j == i + 1):
#             cl[i] = A[i][j]
#     bl[i] = A[i][i]
# alp[0] = -cl[0] / bl[0]
# bet[0] = b[0] / bl[0]
# for i in range(1, n):
#     alp[i] = -cl[i] / (al[i] * alp[i - 1] + bl[i])
#     bet[i] = (bl[i] - al[i] * bet[i - 1]) / (al[i] * alp[i - 1] + bl[i])
# x[n - 1] = (b[n - 1] - al[n - 1] * bet[n - 2]) / (al[n - 1] * alp[n - 2] - bl[n - 1])
# for i, e in reversed(list(enumerate(x))):
#     if (i == n - 1):
#         continue
#     x[i] = alp[i] * x[i + 1] + bet[i]
# print(x)
#
#
# def TDMA(a, b, c, f):
#     a, b, c, f = map(lambda k_list: map(float, k_list), (a, b, c, f))
#
#     alpha = [0]
#     beta = [0]
#     n = len(f)
#     x = [0] * n
#
#     for i in range(n - 1):
#         alpha.append(-b[i] / (a[i] * alpha[i] + c[i]))
#         beta.append((f[i] - a[i] * beta[i]) / (a[i] * alpha[i] + c[i]))
#
#     x[n - 1] = (f[n - 1] - a[n - 2] * beta[n - 1]) / (c[n - 1] + a[n - 2] * alpha[n - 1])
#
#     for i in reversed(range(n - 1)):
#         x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
#
#     return x


# -*- coding: cp1251 -*-


def progonka(a, b):
    N = len(b)
    b[0] /= a[0][0]
    a[0][1] /= -a[0][0]
    for i in range(1, N - 1):
        znam = -a[i][i] - a[i][i - 1] * a[i - 1][i]
        a[i][i + 1] /= znam
        b[i] = (a[i][i - 1] * b[i - 1] - b[i]) / znam
        b[N - 1] = (a[N - 1][N - 2] * b[N - 2] - b[N - 1]) / (-a[N - 1][N - 1] - a[N - 1][N - 2] * a[N - 2][N - 1])
    # зворотний хід
    for i in range(N - 2, -1, -1):
        b[i] += b[i + 1] * a[i][i + 1]
    print(b)


A = [[1, 2, 0, 0], [1, 10, -5, 0, 0], [0, 1, -5, 2], [0, 0, 1, 4]]
b = [-5, -9, -20, -27]

print(progonka(A, b))
