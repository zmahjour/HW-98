import argparse
import pathlib
import os


def get_path_size(input_path, format=None):
    total_size = 0
    if os.path.isfile(input_path):
        total_size += os.path.getsize(input_path)

    elif os.path.isdir(input_path):
        if format:
            for item in os.listdir(input_path):
                if item.endswith(format):
                    new_path = os.path.join(input_path, item)
                    total_size += get_path_size(new_path)

        else:
            for item in os.listdir(input_path):
                new_path = os.path.join(input_path, item)
                total_size += get_path_size(new_path)
        
    return total_size


def convert_B_to_KB(size):
    return f'size: {size/1024:.3f} KB'


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', type=pathlib.Path)
group.add_argument('-f', type=pathlib.Path)
parser.add_argument('-F', type=str)
args = parser.parse_args()

if args.d:
    if args.F:
        print(convert_B_to_KB(get_path_size(args.d, format=args.F)))
    else:
        print(convert_B_to_KB(get_path_size(args.d)))

elif args.f:
    print(convert_B_to_KB(get_path_size(args.f)))


