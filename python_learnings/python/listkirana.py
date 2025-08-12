def kirana():
    items = []
    item_count = int(input("enter itmes number = "))
    
    for i in range(1,item_count+1):
        add = input(f"enter item {i} = ")
        items.append(add)
        
    print("items_list = ",items)
    
    while True:
        
        operations = input("what you want to do ?\n(add/view/update/delete/exit) = ").lower()
        if operations == "add":
            new_items =input("enter the new item add = ")
            items.append(new_items)
            print(f"item{new_items}has been successfully added !")
            
        elif operations == "view":
            print(f"total list is {items}")
            
        elif operations == "update":
            updated_ele = input("enter element you want to update = ")
            if updated_ele in items:
                a = items.index(updated_ele)
                up = input("enter updated element =")
                items[a] = up
                print(items)                
                
            else:
                print(f"{updated_ele} is not found !")
                
        elif operations == "delete":
            delete_ele = input("enter element you want to delete = ")
            if delete_ele in items:
                a = items.index(delete_ele)
                del items[a]
                print(f"updated list = {items}")           
                
            else:
                print(f"{delete_ele} not found !")
                
        elif operations == "exit":
            break
        
        else:
            print("please enter valid options")
kirana()
