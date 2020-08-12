tc = int(input())
for t in range(1, tc+1):
    input_list = list(map(int, input().split()))
    month_date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month1 = input_list[0] - 1
    day1 = input_list[1]
    month2 = input_list[2] - 1
    day2 = input_list[3]
    total = 0
    total2 = 0
    while(month1 > 0):
        total += month_date[month1]
        month1 -= 1
    total += day1

    while(month2 > 0):
        total2 += month_date[month2]
        month2 -= 1
    total2 += day2

    result = total2 - total + 1

    print('#{} {}'.format(t, result))
