#!/usr/bin/python3

"""Module for log parsing script."""
import sys

if __name__ == "__main__":
    size = [0]
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def compute_metrics(line):
        """Computes total size and number of lines per status code"""
        data = line.split(" ")
        size[0] += int(data[-1])
        code = int(data[-2])
        if code in codes:
            codes[code] += 1

    def print_stats():
        """Print statistics"""
        print("File size: {}".format(size[0]))
        for k, v in sorted(codes.items()):
            if v:
                print("{}: {}".format(k, v))
    i = 1
    try:
        for line in sys.stdin:
            compute_metrics(line)
            if i % 10 == 0:
                print_stats()
            i += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
