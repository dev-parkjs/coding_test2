def solution(num_list):
    mult=1
    add=0
    for i in num_list:
        mult*=i
        add+=i
    if mult<add*add:
        return 1
    else:
        return 0
