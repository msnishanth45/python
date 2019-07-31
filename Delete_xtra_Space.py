a = input()
b = [] 
space_flag = False # Flag to check if spaces have occured 
  
for index in range(len(a)): 
  
    if a[index] != ' ': 
        if space_flag == True: 
            if (a[index] == '.' 
                    or a[index] == '?' 
                    or a[index] == ','): 
                pass
            else: 
                b.append(' ') 
            space_flag = False
        b.append(a[index]) 
    elif a[index - 1] != ' ': 
        space_flag = True
  
print (''.join(b))
