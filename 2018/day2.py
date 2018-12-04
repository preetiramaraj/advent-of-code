from collections import Counter

num2 = 0
num3 = 0
with open("day2.txt") as f:
    lines = f.readlines()
    for x in lines:
        count_dict = dict(Counter(x))
        if 2 in count_dict.values():
            num2 = num2 + 1
        if 3 in count_dict.values():
            num3 = num3 + 1
print num2*num3

# Part 2
pairs = {}
for x in lines:
    for y in lines:
        pairs[x,y] = sum(1 for a,b in zip(list(x),list(y)) if a == b) -1


final_pair = pairs.keys()[pairs.values().index(25)]
final_string= ""
for a,b in zip(list(final_pair[0]),list(final_pair[1])):
    if a==b:
        final_string = final_string + a

print final_string
