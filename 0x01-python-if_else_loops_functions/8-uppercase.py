#!/usr/bin/python3
def uppercase(str):
	upper = ""
	for c in str:
		code = ord(c)
		if code > 96 and code < 123:
			upper += chr(code - 32)
		else:
			upper += c
	print(f"{upper:s}")
