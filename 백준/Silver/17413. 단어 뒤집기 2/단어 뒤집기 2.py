S = list(input())


rev_list = []
rev_state = True
result=''
for s in S:
    if s==' ':
        while len(rev_list)>0:
            result+=rev_list.pop()
        result+=s
    elif s=='<':
        rev_state=False
        while len(rev_list)>0:
            result+=rev_list.pop()
        result += s
    elif s=='>':
        rev_state=True
        result += s
    elif not rev_state:
        result += s

    if rev_state:
        if not s==' ' and not s=='>':
            rev_list.append(s)
            continue


while len(rev_list) > 0:
    result += rev_list.pop()

print(result)