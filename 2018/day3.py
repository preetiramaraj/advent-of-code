from collections import defaultdict

data = defaultdict(list)
cloth_dict = defaultdict(int)
with open("day3.txt") as f:
    lines = f.readlines()

for x in lines:
    list_x = x.split()
    # top-left corner
    y_init,x_init = [int(l) for l in list_x[2][:-1].split(',')]
    w,h = list_x[3].split('x')
    for i in range(int(h)):
        for j in range(int(w)):
            cloth_dict[x_init+i, y_init+j] += 1

print len([val for val in cloth_dict.values() if val >= 2])
	