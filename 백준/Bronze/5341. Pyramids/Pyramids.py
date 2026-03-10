while True:
    a = int(input())
    if not a:
        break
    print(sum([x for x in range(a+1)]))