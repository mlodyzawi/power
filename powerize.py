import argparse
from time import perf_counter

parser = argparse.ArgumentParser(description='Calculate a power of given number')
parser.add_argument('-n', '--your_number', required=True, type=int, metavar='', help='that\'s where your number goes!')
args = parser.parse_args()

def powerize(x):
    result = 1
    for i in range(1,x):
        result=result*i
    return result

if __name__ == '__main__':
    timestart = perf_counter()
    print(f'power of {args.your_number} equals {powerize(args.your_number)}')
    timestop = perf_counter()
    print(f'time used to compute the power of {args.your_number}: {timestop - timestart} seconds')
