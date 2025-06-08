n=int(input())
s=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
while s and c<len(s):
    if s[0]==b[0]:s.pop(0);b.pop(0);c=0
    else:s.append(s.pop(0));c+=1
print(len(s))