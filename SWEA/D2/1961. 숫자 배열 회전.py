tc = int(input())
for t in range(tc):
    N = int(input())
    for a in range(N):
        input_arr = [[0] * N for _ in range(N)]
    for b in range(N):
        input_arr[b] = list(map(int, input().split()))

    degree90 = [[0] * N for _ in range(N)]

    for c in range(N):
        for d in range(N):
            degree90[d][N-1-c] = input_arr[c][d]

    degree180 = [[0] * N for _ in range(N)]
    for e in range(N):
        for f in range(N):
            degree180[f][N-1-e] = degree90[e][f]

    degree270 = [[0] * N for _ in range(N)]
    for g in range(N):
        for h in range(N):
            degree270[h][N-1-g] = degree180[g][h]

    res90 = ''
    res180 = ''
    res270 = ''

    for z in range(N):
        res90 += "".join(map(str, degree90[z]))
        res90 += " "
    print(res90)
    for x in range(N):
        res180 += "".join(map(str, degree180[x]))
        res180 += " "
    print(res180)
    for y in range(N):
        res270 += "".join(map(str, degree270[y]))
        res270 += " "
    print(res270)
    # print(res90)
    # print(res180)
    # print(res270)

    res = []
    res += map(int, res90.split())
    print(res)
    res += map(int, res180.split())
    print(res)
    res += map(int, res270.split())
    print(res)

    last = []

    for i in range(N):
        last.append(res[i::N])
    print(last)
    print('#{}'.format(tc))
    for A in range(3):
        print("")
        for B in range(6):
            print(last[A][B], end=" ")


# for idx in range(1, int(input())+1):
#     N = int(input())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     print('#{}' .format(idx))
#     for i in range(N):
#         for j in range(N):
#             print(lst[N-j-1][i], end='')
#         print('', end=' ')
#         for k in range(N):
#             print(lst[N-i-1][N-k-1], end='')
#         print('', end=' ')
#         for l in range(N):
#             print(lst[l][N-i-1], end='')
#         print()
