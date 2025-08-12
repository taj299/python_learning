"""
condition -
odd = 1 3 5 7
even = 0 2 4 6

"""

number = float (input("enter a number to check = "))
  
if number %2 == 0:
    print(f"entered number {number} even")

else:
        print(f"entered number {number} odd")