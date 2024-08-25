def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
list=[100,2,3,1,3,5,1,90,45,23,78,34,100,0,34,90]
sort(list)
print("sorted list",list)