weight = float(input("enter your weight : "))
unit =input("kilograms or pounds ? (k or L ):")

if unit == "k":
    
    weight = weight*2.205
    unit = "LBS"
    print(f"your weight is :{round (weight,1)} {unit} ")
    
elif unit == "L":
    
    weight = weight/2.205
    unit = "KGS"
    print(f"your weight is :{round (weight,1)} {unit} ")
    
else:
    print(f"{unit} was not valid ")