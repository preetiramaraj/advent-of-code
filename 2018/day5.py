from copy import deepcopy
	
with open("day5.txt") as f:
    line = f.readline().strip()
	
def react(str):
	str_array = list(str)
	diff_array = [ord(str_array[i])-ord(str_array[i+1]) for i in range(0,len(str_array)-1)]
	#print diff_array
	while 32 in diff_array or -32 in diff_array:
		length = len(str_array)
		index = min(diff_array.index(32) if 32 in diff_array else 99999, diff_array.index(-32) if -32 in diff_array else 99999)
		if index == 99999:
			break
		del str_array[index:index+2]
		if index == 0:
			del diff_array[index:index+2]
		else:
			del diff_array[index-1:index+1]
		if index > 0 and index < (length-2):
			diff_array[index-1] = ord(str_array[index-1]) - ord(str_array[index])

	return len(str_array)

alphabet = set([x.lower() for x in line])

# Part 1
print react(line)
# Non-optimized part 2
original_line = deepcopy(line)
lengths = {}
for x in alphabet:
	print x
	line = deepcopy(original_line)
	lengths[x] = react((line.replace(x,'').replace(x.upper(),'')))
print min(lengths.values())







