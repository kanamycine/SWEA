a = int(input())

for i in range(a):
    b, c = map(int, input().split())
    input_list_1 = list(map(int, input().split()))
    input_list_2 = list(map(int, input().split()))
    tmp = []
    if len(input_list_1) > len(input_list_2):
        tmp = input_list_1
        input_list_1 = input_list_2
        input_list_2 = tmp
    

    cycle = abs(b - c) + 1
    
    result_list = []
    for k in range(cycle):
        total = 0
        for j in range(len(input_list_1)):
            total += input_list_1[j] * input_list_2[j]
        result_list.append(total)
        input_list_2.remove(input_list_2[0])
    print(f'#{i + 1} {max(result_list)}')    
    