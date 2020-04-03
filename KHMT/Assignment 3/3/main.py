import sys
import math
import string
sys.stdin = open('D:/code/KHMT/Assignment 3/3/INP.txt', 'r')

N = int(input())
v = list(map(int, input().split()))
v.sort()
cnt = 0
for i in range(N-1):
    cnt += v[i+1] - (v[i] + 1)
print(cnt)