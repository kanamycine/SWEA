
'''
a[n][1] = 1
a[n][n] = 1
a[n][k] = a[n-1][k-1] + a[n-1][k] (n, k >= 0)
'''
tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    arr = [[1], [1, 1]]
    for n in range(3, N+1):
        tmp = [0] * n
        tmp[0] = tmp[n-1] = 1
        for i in range(1, n-1):
            tmp[i] = arr[n-2][i-1] + arr[n-2][i]
        arr.append(tmp)
    print('#%d' % t)
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()
