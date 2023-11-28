#!/usr/bin/python3
for i in range(10):
	for j in range(i, 10):
		if i == 8 and j == 9:
			print(f"{(i*10 + j):02d}")
		elif (i != j):
			print(f"{(i*10 + j):02d},", end=" ")
