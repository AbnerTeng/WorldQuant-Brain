import argparse


# parser = argparse.ArgumentParser()
# parser.add_argument('-a', required=True)
# parser.add_argument('-b', required=True)
# parser.add_argument('-c', required=True)
# parser.add_argument('-d', required=True, type=int, nargs='+')

# args = parser.parse_args()

# print(args.a, args.b, args.c)
# print(args.d)

file = './test.csv'
with open(file, 'a') as f:
    f.write('test\n')