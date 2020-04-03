import math
import string
import bisect
import sys
sys.stdin = open('D:/code/KHMT/Assignment 3/9/INP.txt', 'r')

n, m = map(int, input().split())
a = len(str(n))
cnt = 0
while n<=m:
    if n <= m:
        cnt += 1
    n = n + 10**(a)
print(cnt)
    