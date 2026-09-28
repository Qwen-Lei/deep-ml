def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]|int:
    m = len(a)
    n = len(a[0]) if m > 0 else 0
    if len(b) != n:
        return -1
    p = len(b[0]) if n > 0 else 0
    c = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c