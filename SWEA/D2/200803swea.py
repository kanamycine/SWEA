a = int(input())
for i in range(a):
    N = int(input())
    end_condition = ["0","1","2","3","4","5","6","7","8","9"]
    count = 0
    while(end_condition):
        count += 1
        str_N = N * count
        str_N = str(str_N)

        for j in str_N:
            if j in end_condition:
                end_condition.remove(j)

        
    
    print(f'#{i+1} {str_N}')