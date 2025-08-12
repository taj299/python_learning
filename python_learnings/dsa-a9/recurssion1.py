def fun(x):
    if x <= 10:
        print(x)
        fun(x*2)
        
print(fun(1))

#------> 


def fun(x):
    if x >= 10:
        print(x)
        fun(x-2)
        
print(fun(20))