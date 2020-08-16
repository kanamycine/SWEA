tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    nums = [n for n in range(1, N**2 + 1)]
    arr = [[0] * N for _ in range(N)]

    x, y = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0  # 0 : right, 1 : down , 2 : left , 3 : up

    for i in range(N**2):
        arr[x][y] = nums[i]
        x += dx[direction]
        y += dy[direction]
        if x < 0 or x > N-1 or y < 0 or y > N-1 or arr[x][y]:
            x -= dx[direction]
            y -= dy[direction]
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]
    print('#{}'.format(t))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
