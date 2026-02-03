input_str = input()

rule = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for r in rule:
    if r in input_str:
        input_str = input_str.replace(r, 'a')

print(len(input_str))
