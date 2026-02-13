def string_rep(s):
    for c in s:
        if c.isalpha() or c=='-':
            continue
        else :
            s=s.replace(c,'')
    return s
max_s=''
max_len=-float('inf')
while True:
    try:
        s_list = input().split()
        for a in range(len(s_list)):
            s_list[a]=string_rep(s_list[a])
        a_list = list(map(len,s_list))
        for a in a_list:
            if max_len<a:
                max_len=a
                max_s=s_list[a_list.index(a)]
    except EOFError:
        break
print(max_s.lower())