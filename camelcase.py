# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
s = str(input())
upp = [i.capitalize() for i in s.split()]
print(" ".join(upp))