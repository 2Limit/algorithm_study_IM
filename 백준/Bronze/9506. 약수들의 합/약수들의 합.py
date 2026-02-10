while True:
    num = int(input())
    if num==-1:
        break
    div_list=[]
    for i in range(1,num):
        if num%i==0:
            div_list.append(i)
    result = str(num)+' '
    if sum(div_list)==num:
        result+='= '
        result+= ' + '.join(map(str,div_list))
    else :
        result+='is NOT perfect.'
    print(result)