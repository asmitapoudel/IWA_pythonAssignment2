#to check whether the number is prime or not
def is_Prime(n) : 
  
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
  
 
if (is_Prime(11)) : 
    print(" true") 
else : 
    print(" false") 
      
if(is_Prime(15)) : 
    print(" true") 
else :  
    print(" false") 
      