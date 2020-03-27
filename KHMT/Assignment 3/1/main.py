import sys
import math
sys.stdin = open('D:/code/KHMT/Assignment 3/1/INP.txt', 'r')

N = int(input())
x, y = map(int, input().split())
disw = math.sqrt((x - 1)**2 + (y - 1)**2)
disb = math.sqrt((N - x)**2 + (N - y)**2)
#print(" {} {}".format(disw,disb))
if disw == disb:
    print("White")
elif disw < disb:
    print("White")
else:
    print ("Black")
