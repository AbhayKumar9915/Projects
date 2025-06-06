def RevSumInteger(num):
    rev_num = 0
    sum_num = 0
    while num != 0:
        temp = num % 10
        rev_num = rev_num * 10 + temp
        sum_num = sum_num + temp
        num = num // 10
    return rev_num,sum_num


print(RevSumInteger(1458))
