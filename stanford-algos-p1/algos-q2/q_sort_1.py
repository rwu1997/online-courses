import fileinput

n_comps = 0

def quick_sort(arr):
	global n_comps
	n_comps += len(arr) - 1

	pivot = arr[0]

	i = 0
	j = 1
	
	while j < len(arr):
		if (arr[j] < pivot):
			i += 1
			if (j > i):
				arr[j], arr[i] = arr[i], arr[j]
		j += 1
	
	arr[0], arr[i] = arr[i], arr[0]
	
	if i > 0:
		left = quick_sort(arr[:i])
	else:
		left = []
	
	if i < len(arr) - 1:
		right = quick_sort(arr[i+1:len(arr)])
	else:
		right = []
	
	return left + [pivot] + right

arr = []

for line in fileinput.input():
	arr.append(int(line))

sorted_arr = quick_sort(arr)

print n_comps