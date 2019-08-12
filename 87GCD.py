mm,gg = list(map(int,input().strip().split()))[:2] 
i=1
while(i <= mm and i <= gg):
    if(mm % i == 0 and gg % i == 0):
        gcd = i
    i = i + 1
print(gcd) 
