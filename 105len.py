a=int(input())
m=str(a)
cc=len(m)
sum=0
while(a>0):
  r=a%10
  sum=sum+r**cc
  a=a//10
print(sum)