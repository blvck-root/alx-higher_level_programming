#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    for num in argv[1:]:
        total += int(num)
    print(total)
