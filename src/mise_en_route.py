#!/usr/bin/env python3

i = 0
sum_of_squares = 0

while i < 10:
	i = i + 1
	sum_of_squares = sum_of_squares + i * i

	print(i, '\t', i * i, '\t', sum_of_squares, '\t', i * (i + 1) * (2 * i + 1) // 6)
