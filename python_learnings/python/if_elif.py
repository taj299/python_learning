marks = int(input("Enter your grade: "))

if marks >= 90 and marks <= 100:
    print("Grade A")

elif marks >= 80 and marks < 90:
    print("Grade B")

elif marks >= 60 and marks < 80:
    print("Grade C")

elif marks >= 40 and marks < 60:
    print("Grade D")

elif marks >= 33 and marks < 40:
    print("Grade E")

elif marks >= 0 and marks < 33:
    print("TRY AGAIN! > 33")

else:
    print("Invalid input. Marks should be between 0 and 100.")
    
    
    
    '''def insertionInBST(ptr,val):
    if ptr==None:
        newnode=Tree(val)
        return newnode
    elif ptr.data>val:
        ptr.left=insertionInBST(ptr.left,val)
    elif ptr.data<val:
        ptr.right=insertionInBST(ptr.right,val)
        '''
     
         
    