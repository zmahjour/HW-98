import sys


grades = [int(sys.argv[i]) for i in range(1, len(sys.argv))]
print(f"average: {sum(grades) / len(grades)}")

    