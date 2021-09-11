import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# Ввод, если два числа и более в одну строку
for i in range(5):
    (a, b, c) = [int(s) for s in input().split()]
    if 0<=a<=23:
        if 0<=b<60 and 0<=c<60:
                print("YES")
        else:
                print("NO")
    else:
            print("NO")