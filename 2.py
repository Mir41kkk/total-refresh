import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a = int(input())
if a>0:
    if a%2==0:
        print("YES")
        print(a+2)
    else:
        print("NO")
        print(a+1)
else:
    print("NO")
    print(2)