def values(lst):
    size=int(input("enter the size of list"))
    for i in range(size):
        items=input("enter the name in the list")
        lst.append(items)
    print(lst)

    for e in lst:
        if len(e)>=5:
            print(f"{e} is the one of the name in the list which contain more than 5 characters")
            
    else:
        
        print(f"{e} is the one of the name in the list which not contain more than 5 characters") 

lst=[]

values(lst)

