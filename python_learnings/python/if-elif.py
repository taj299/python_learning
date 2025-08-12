Marks=float(input("Enter marks out of 100"))
if Marks<1 or Marks>100:
    print("ENter marks again")
elif Marks>=90:
    print("A")
elif Marks>=80:
    print("B")
elif Marks>=60:
    print("C")
elif Marks>=40:
    print("D")
elif Marks>=33:
    print("E")
else:
    print("Try again")