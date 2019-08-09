n=int(input())
x=1
y=1
count=0
while(count<n):
    print(x,end=' ')
    c=x+y
    x=y
    y=c
    count+=1
