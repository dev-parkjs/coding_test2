def solution(myString):
    answer = ''
    for j in myString:
        if j<'l':
            answer+='l'
        else:
            answer+=j
    return answer