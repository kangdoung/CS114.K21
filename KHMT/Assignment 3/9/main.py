import math
import string
import bisect
import sys
#sys.stdin = open('D:/code/KHMT/Assignment 3/9/INP.txt', 'r')

n, m = map(int, input().split())
a = len(str(n))
check = str(m)
x = len(str(m))
nstr = ''
for i in range(a):
    nstr = check[len(check) - 1 -i] +  nstr 
ans = 0
if int(nstr) >= n:
    ans += 1
cur = 1
mm = str(m)
#print(mm)
for i in range(a,x):
    #print(mm[x - 1 - i])
    ans += int(mm[x - 1 - i])*cur 
    #print("{} {}".format(int(mm[x - 1 - i]), ans))
    cur = cur*10
print(ans)

    

    