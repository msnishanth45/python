x,y,z = list(map(int,input().strip().split()))[:3] 
if x>y and x>z:
  print(x)
elif y>z:
  print(y)
else:
  print(z)
