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
            data[x_init+i, y_init+j].append(list_x[0])

# Part 1
print len([val for val in cloth_dict.values() if val >= 2])
# Part 2
lists_of_ids = set([item for sublist in [val for val in data.values() if len(val) > 1] for item in sublist])
int_list_of_ids = [int(l.replace('#','')) for l in lists_of_ids]
print list(set(list(range(1,1311))).difference(list(int_list_of_ids)))
	