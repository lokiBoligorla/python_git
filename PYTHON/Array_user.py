from array import *
demo=array("i",[])
x=int(input("enter the length of the array "))

for i in range(x):
    new=int(input("enter the elements in array "))
    demo.append(new)
print(demo)  

particular_ele=int(input("enter th element do you want to search "))
for e in demo:
    if particular_ele==e:
        print("index is",demo.index(particular_ele))
        break
else:
    print("element was not found ")    