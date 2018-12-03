from copy import deepcopy

final_val = 0
i = 0
with open("day1.txt") as f:
    sum_list = []
    for x in f.readlines():
        final_val = final_val + int(x[1:]) if x[0]=='+' else final_val - int(x[1:])
        sum_list.append(final_val)

# Part 2
new_list = deepcopy(sum_list)
while len(new_list) == len(set(new_list)):
    iteration_list = [(x+final_val) for x in sum_list]
    new_list = deepcopy(new_list + iteration_list)
    sum_list = deepcopy(iteration_list)

old_list = new_list[:-len(iteration_list) or None]
final_duplicate_list = [(i,x) for i,x in enumerate(iteration_list) if x in iteration_list and x in old_list]
print final_duplicate_list[0]

    
