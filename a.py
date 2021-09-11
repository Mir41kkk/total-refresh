import math
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
(a, b, c) = [int(s) for s in input().split()]
(h, l,) = [int(s) for s in input().split()]
o = (a * b + a* c + b*c)*2-a*b
o = o - 0.15*o
v = h*0.001
p = l*0.001
j = v *p
j = j - 0.1 * j
u = o/j
print(math.ceil(u))