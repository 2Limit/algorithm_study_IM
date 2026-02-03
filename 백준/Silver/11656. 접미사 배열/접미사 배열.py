input_str = input()

pop_list = []
for i in range(len(input_str)):
    pop_list.append(input_str[i:])

pop_list = sorted(pop_list)
for p in pop_list:
    print(p)