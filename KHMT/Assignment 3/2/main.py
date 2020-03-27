import sys
import math
import string
sys.stdin = open('D:/code/KHMT/Assignment 3/2/INP.txt', 'r')

def sol(N,s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == "8":
            cnt += 1
        if cnt*11 > N:
            return cnt-1
        elif cnt*11 == N:
            return cnt
    return cnt


N = int(input())
s = input()
ans = sol(N,s)
print(ans)
