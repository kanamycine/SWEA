tc = int(input())
for t in range(tc):
    N, K = map(int, input().split())
    arr = [0] * N
    for n in range(N):
        arr[n] = list(map(int, input().split()))
    cnt = 0 
    gotcha = 0
    result=0

    print(arr)

    while(cnt < N):
        for a in range(N):
            for b in range(N):
                if arr[a][b] == 1: 
                    gotcha += 1
            
                if gotcha == K :
                    if arr[a][b+1] == 0:
                        result += 1
                        gotcha = 0
        cnt += 1
    print(result)