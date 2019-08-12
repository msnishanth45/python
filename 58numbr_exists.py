c,d=map(int,input().split())
p=list(map(int,input().strip().split()))[:c]
if d in p:
  print("yes")
else:
  print("no")
