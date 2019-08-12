n1,n2=map(int,input().split())
lcm = n1 if(n1 > n2) else n2
while(True):
    if((lcm % n1 == 0) and (lcm % n2 == 0)):
        print(lcm)
        break
    lcm += 1
