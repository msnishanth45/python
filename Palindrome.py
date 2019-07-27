x=int(input())
m=x
i=0
while(x>0):
  r=x%10
  i=i*10 + r
  x=x//10
if(i==m):
  print("yes")
else:
  print("no")
