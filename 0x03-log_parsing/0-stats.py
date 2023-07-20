#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:

"""

import sys
from collections import defaultdict

def parse_line(line):
    try:
        _, _, _, _, _, status_code, file_size = line.split()[0:7]
        return int(status_code), int(file_size)
    except (ValueError, IndexError):
        return None, None

def print_statistics(total_file_size, status_counts):
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_file_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line.strip())
            if status_code is not None and file_size is not None:
                total_file_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_file_size, status_counts)
    except KeyboardInterrupt:
        print("\nKeyboard interruption received. Printing current statistics.")
        print_statistics(total_file_size, status_counts)

if __name__ == "__main__":
    main()
