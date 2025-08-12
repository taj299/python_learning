def fact(n): #----> function <-----
    
    if n<=1: # call function check condition true hori kya nahi 
        return 1
    
    else:
        return n*fact(n-1)
    
print(fact(7))