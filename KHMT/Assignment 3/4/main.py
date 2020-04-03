import sys
import math
import string
#sys.stdin = open('D:/code/KHMT/Assignment 3/4/INP.txt', 'r')

def sol(s,t):
    cnt = [ 0 for _ in range(300)]
    if s==t:
        return ("YES")
    for i in range(len(s)):
        if cnt[ord(s[i])] == 0:
           cnt[ord(s[i])] = 1
    for i in range(len(t)):
        if cnt[ord(t[i])] == 1:
            return ("YES")
    return ("NO")


Q = int(input())
for tc in range(Q):
    s = input()
    t = input()
    ans = sol(s,t)
    print(ans)
    