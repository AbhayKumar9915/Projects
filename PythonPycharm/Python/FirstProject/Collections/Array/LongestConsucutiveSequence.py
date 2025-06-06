l = [100, 4, 101, 102, 1, 3, 103, 2, 104]

def longestCS(lst):
    lst_set = set(lst)
    longest_seq = 0
    for i in lst:
        if i-1 not in lst_set:
            cur_num  = i
            current_seq = 1
            while cur_num+1 in lst_set:
                cur_num += 1
                current_seq += 1
            longest_seq = max(longest_seq,current_seq)
    return longest_seq

print(longestCS(l))