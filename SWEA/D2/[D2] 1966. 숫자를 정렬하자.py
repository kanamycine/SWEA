tc = int(input())
for t in range(1, tc+1):
    list_num = int(input())
    input_list = list(map(int, input().split()))
    tmp = 0
    
    for j in range(list_num):
        for i in range(list_num - 1):
            if input_list[i] > input_list[i+1]:
                tmp = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i+1] = tmp

    print('#{}'.format(t), end= " ")
    for k in range(len(input_list)):
        print('{}'.format(input_list[k]), end = " ")
    print()
