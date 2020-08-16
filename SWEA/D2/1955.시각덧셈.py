tc = int(input())
for t in range(1, tc+1):
    input_list = list(map(int, input().split()))
    result_list = []

    hour = input_list[0] + input_list[2]
    minute = input_list[1] + input_list[3]

    if minute > 59:
        minute = minute % 60
        hour += 1

    if hour > 12:
        hour = hour % 12

    if hour == 0:
        hour = 12

    print('#{}'.format(t), hour, minute, end=" ")
    print('')
