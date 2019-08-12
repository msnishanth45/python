    
j,k=map(int,input().split())
m=list(map(int,input().strip().split()))[:j]
if k in m:
  c=m.count(k)
  print(c)
else:
  print("0")  
