def largest_even(lst):
	max=0
	for i in lst:
		if i%2==0 and i>max:
			max=i
	if max==0:
		return -1
	return max

print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))
print(largest_even([1, 3, 5, 7]))
print(largest_even([0, 19, 18973623]))

