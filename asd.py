import sys

a= int(input())

for _ in range(0,a):
    x,y=sys.stdin.readline().rsplit()
    x=int(x)
    y=int(y)
    print(x+y)
