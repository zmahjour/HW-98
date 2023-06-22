import argparse


parser = argparse.ArgumentParser()

parser.add_argument('-g', '--grades', help='your grades', type=float, nargs='+', required=True)
parser.add_argument('-f', '--float', help='number of decimal places', type=int, default=2)

args = parser.parse_args()
average = sum(args.grades) / len(args.grades)
print(f'average: {average:.{args.float}f}')


