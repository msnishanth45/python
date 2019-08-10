nn=int(input())
a=list(map(int,input().split()))[:nn]
c=0
for i in range(nn):
    c+=a[i]
d=c//nn
print(d)
