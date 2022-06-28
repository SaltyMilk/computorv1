def mysqrt(n):
	lo = n if n < 1 else 1
	hi = n if n > 1 else 1

	while (100 * lo * lo < n):
		lo *= 10
	while (0.01 * hi * hi > n):
		hi *= 0.1

	i = 0
	while i < 100:
		mid = (lo + hi) / 2
		if mid * mid == n:
			return mid
		if mid * mid > n:
			hi = mid
		else:
			lo = mid
		i += 1

	return mid
from math import sqrt

print(sqrt(164.8))
print(mysqrt(164.8))
