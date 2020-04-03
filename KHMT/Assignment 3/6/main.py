import math
import string
import bisect
sys.stdin = open('D:/code/KHMT/Assignment 3/6/INP.txt', 'r')


def sol(n, k, v):
    cnt = 0
    if v[0] == 0:
        return 0
    elif (k==n) and (v[k-1] != 0):
        return n
    elif v[k-1] == 0:
        for i in range(k):
            if v[i] == 0:
                cnt = i
                return cnt 
    else:
        for i in range(k-1,n):
            if v[i] < v[k-1]:
                cnt = i
                return cnt
        

n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = sol(n,k,v)
print(ans)
