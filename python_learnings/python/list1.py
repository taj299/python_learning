def lst():
    
    start = int(input("where you want to start ="))
    stop =int(input("where you want to stop ="))
    step =int(input("enter step size ="))
    
    my_list =list(range(start,stop + 1,step))
    print(my_list)
    
    for i in range(start,stop + 1,step):
        print(i)
        
lst()