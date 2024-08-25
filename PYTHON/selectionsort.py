def sort(list):
    for i  in range(len(list)-1):
        minpos=i
        for j in range(i,len(list)):
            if list[j]< list[minpos]:
                minpos=j

    temp=list[i]    # Swapping two numbers
    list[i]=list[minpos]
    list[minpos]=temp        


list=[3,2,5,4,90,78,65,32,11,2,39]
sort(list)
print(list)