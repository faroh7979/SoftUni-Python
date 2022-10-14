from math import log, e

num = int(input())
base_input = input()

base = e if base_input == 'natural' else int(base_input)

print(f'{log(num, base):.2f}')
