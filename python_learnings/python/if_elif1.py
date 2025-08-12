"""
marks 1 to 100
100 > 90 A
80 > 90  B
60 > 80  c
40 > 60  D
33 > 40  E
TRY AGAIN! > 33

invalid input
"""


marks = int(input("Enter your marks:"))
 
if 90 > marks <= 100:
    print("marks A")

elif  80 <= marks <90:
    print("marks B")

elif 60 <= marks <80:
    print("marks C")

elif 40<= marks <60:
    print("marks D")

elif 33<= marks <40:
    print("marks E")

elif 0 <= marks <33:
    print("TRY AGAIN! > 33")

else:
    print("Invalid input")