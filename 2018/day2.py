from collections import Counter

num2 = 0
num3 = 0
with open("day2.txt") as f:
    for x in f.readlines():
        count_dict = dict(Counter(x))
        if 2 in count_dict.values():
            num2 = num2 + 1
        if 3 in count_dict.values():
            num3 = num3 + 1
print num2*num3
