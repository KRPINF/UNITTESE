from math import sqrt
def i_sqrt(n):
	if n > 0:
		count = 0
		while n >= 2:
			count += 1
			n = sqrt(n)
		return count
	return 'invalid'

print(i_sqrt(1))
print(i_sqrt(2))
print(i_sqrt(7))
print(i_sqrt(27))
print(i_sqrt(256))
print(i_sqrt(-1))