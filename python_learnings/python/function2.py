
while True:       
    n = int(input("enter number : "))
    i = 0
    while i <= n:
        print(i)
        i += 1
            
    stop = input("do you want to stop YES/NO :")
    if stop == "YES":
        break
    else:
        continue
        