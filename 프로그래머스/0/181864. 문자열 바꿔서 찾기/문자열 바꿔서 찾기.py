def solution(myString, pat):
    answer = ""
    for i in myString:
        if i == "A":
            answer += "B"
        elif i == "B":
            answer += "A"
    
    return 1 if pat in answer else 0
