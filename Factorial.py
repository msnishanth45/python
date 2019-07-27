num1 = int(input())
factoriall = 1
if num1 == 0:
   print(1)
else:
   for i in range(1,num1 + 1):
       factoriall = factoriall*i
   print(factoriall)
