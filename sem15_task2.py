import argparse
import decimal
import math

parser = argparse.ArgumentParser(description='Calculate the area of a circle and the circumference')
parser.add_argument('-d', type=int, default=66)
args = parser.parse_args()


def area(d):
    decimal.getcontext().prec = 42
    pi = decimal.Decimal(str(math.pi))
    d = decimal.Decimal(str(d))
    return pi * (d / 2) ** 2


def len_circle(d):
    decimal.getcontext().prec = 42
    pi = decimal.Decimal(str(math.pi))
    d = decimal.Decimal(str(d))
    return pi * d


print(area(args.d))
print(len_circle(args.d))
