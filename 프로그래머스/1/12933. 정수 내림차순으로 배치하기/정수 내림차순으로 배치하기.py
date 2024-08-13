def solution(n):
    a=list(str(int(n)))
    a.sort(reverse=True)
    return int("".join(a))
