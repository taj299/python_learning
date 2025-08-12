def square():
    user = []
    num = int(input("enter how many element = "))
    i = 1
    for i in range(num +1):
        element = int(input(f"enter number list {num} = "))
        user.append (element ** 2)
    print("updated list = ",user)
    
square()