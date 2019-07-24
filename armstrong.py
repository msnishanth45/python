a,b = map(int,input().split())
 
for n in range(a,b + 1):
   # initialize sum
   sum = 0
 
   # find the sum of the cube of each digit
   temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if n == sum:
       print(n)
