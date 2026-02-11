# 3**n개 만큼의 -문자가 존재
# 삼등분으로 - - 이 되게끔 중앙 공백화
# 시작점 -------
# 분배할까?
# 종료점 len(list) ==1
# 행동 : - ' ' - 의 삼등분 을 반복
def make_canto(iter):
    if len(iter)==1:
        result.append(iter[0])
        return
    make_canto(iter[:int(len(iter)/3)])
    a= iter[int(len(iter)/3):int(len(iter)/3*2)]
    a= a.replace('-',' ')
    result.append(a)
    make_canto(iter[int(len(iter)/3*2):len(iter)])

while True:
    try :
        num = int(input())
    except:
        break
    bar ='-'*(3**num)
    result=[]
    make_canto(bar)
    print(''.join(result))