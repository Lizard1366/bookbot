from stats import print_report
import sys

def main(path_to_book):
    return print_report(path_to_book)

if len(sys.argv) > 1:
    main(sys.argv[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)