import sys
input = sys.stdin.readline

n = int(input())

l = [int(input()) for _ in range(n)]

l.sort()

for n in l:
    print(n)