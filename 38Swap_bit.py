j,o=list(map(int,input().strip().split()))[:2]
j=j^o
o=j^o
j=j^o
print(j,o)
