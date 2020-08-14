tc = int(input())
for t in range(tc):
    a, b = map(int, input().split())
    
    
    input_list = [[0] * a for _ in range(a)]
    

    for a in range(a):
        input_list[a] = list(map(int, input().split()))
    
    ans = 0
    for b in range(a): 
        rowcnt = 0 
        colcnt = 0
        for c in range(a):
            if input_list[b][c] == 1:
                rowcnt += 1
            elif input_list[b][c] == 0:
                if rowcnt == b:
                    ans += 1
                rowcnt = 0   
            




