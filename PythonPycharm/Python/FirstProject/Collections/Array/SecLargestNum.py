def sec_large(lst):
    m1, m2 = lst[0], lst[1]
    for x in lst[2:]:
        if x > m2:
            if x > m1:
                m2, m1 = m1, x
            else:
                m2 = x
    return m2


print("Sec Largest Num: ", sec_large([6, 2, 5, 8, 4, 7, 9]))
