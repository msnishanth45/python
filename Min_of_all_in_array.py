a,b=map(int,input().split())
c=(input().split())[0:a] 
i=0
while i<b:
  d,e=map(int,input().split())
  i+=1
  print(min(c[d-1:e])) 
