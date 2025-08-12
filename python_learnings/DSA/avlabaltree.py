class Tree:
    left=None
    right=None
    data=None
    height=1
    def __init__(self,data):
        self.data=data

def inOrder(ptr):
    if ptr==None:
        return None
    else:
        inOrder(ptr.left)
        print(ptr.data)
        inOrder(ptr.right)
 
def getheight(ptr):
    if ptr==None:
        return 0
    return ptr.height

def getBalance(ptr):
    if ptr==None:
        return 0
    return getheight(ptr.left)-getheight(ptr.right)

def rightRotate(y):
    x=y.left
    t2=x.right
    x.right=y
    y.left=t2
    
    y.height=max(getheight(y.left),getheight(y.right))+1
    x.height=max(getheight(x.left),getheight(x.right))+1
    return x

def leftRotate(x):
    y=x.right
    t2=y.left
    y.left=x
    x.right=t2
    
    x.height=max(getheight(x.left),getheight(x.right))+1
    y.height=max(getheight(y.left),getheight(y.right))+1
    return y      
def insertionInAVL(ptr,val):
    if ptr==None:
        newnode=Tree(val)
        return newnode
    elif ptr.data>val:
        ptr.left=insertionInAVL(ptr.left,val)
    elif ptr.data<val:
        ptr.right=insertionInAVL(ptr.right,val)
        
    ptr.height=1+max(getheight(ptr.left),getheight(ptr.right))

    balance=getBalance(ptr)
    if balance>1:
        if getBalance(ptr.left)>=0:
            return rightRotate(ptr)
        else:
            ptr.left=leftRotate(ptr.left)
            return rightRotate(ptr)
    
    if balance<-1:
        if getBalance(ptr.right)<=0:
            return leftRotate(ptr)
        else:
            ptr.right=rightRotate(ptr.right)
            return leftRotate(ptr)
    return ptr



def findSuccessor(ptr):
    copy=ptr
    while copy.left!=None:
        copy=copy.left
    return copy
def deleteInAVL(ptr,sval):
    if ptr==None:
        return ptr
    elif ptr.data>sval:
        ptr.left=deleteInAVL(ptr.left,sval)
    elif ptr.data<sval:
        ptr.right=deleteInAVL(ptr.right,sval)
    else:
        if ptr.left==None:
            temp=ptr.right
            ptr=None
            return temp
        if ptr.right==None:
            temp=ptr.left
            ptr=None
            return temp
        
        temp=findSuccessor(ptr.right)
        ptr.data=temp.data
        ptr.right=deleteInAVL(ptr.right,temp.data)
        
    ptr.height=1+max(getheight(ptr.left),getheight(ptr.right))

    balance=getBalance(ptr)
    if balance>1:
        if getBalance(ptr.left)>=0:
            return rightRotate(ptr)
        else:
            ptr.left=leftRotate(ptr.left)
            return rightRotate(ptr)
    
    if balance<-1:
        if getBalance(ptr.right)<=0:
            return leftRotate(ptr)
        else:
            ptr.right=rightRotate(ptr.right)
            return leftRotate(ptr)
    return ptr 


a=None
a=insertionInAVL(a,33)
a=insertionInAVL(a,13)
a=insertionInAVL(a,53)
a=insertionInAVL(a,11)
a=insertionInAVL(a,21)
a=insertionInAVL(a,61)
a=insertionInAVL(a,8)
a=insertionInAVL(a,9)

inOrder(a)

