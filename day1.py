final_val = 0
i = 0
with open("day1.txt") as f:
    i = 0
    for x in f.readlines():
        final_val = final_val + int(x[1:]) if x[0]=='+' else final_val - int(x[1:])

print final_val