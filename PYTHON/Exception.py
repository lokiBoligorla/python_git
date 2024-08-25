a=30
b=0
nums=[1,2,3,4]
try:
    print("resource is open")
    print(a/b)
    print(nums[5])
    K=int(input("enter the string"))
    print(K)
except ZeroDivisionError as e:
    print("you cannot divide by a number",e)

except IndexError as e:
    print("index was out of bound",e)   
except ValueError as e:
    print("wrong input",e) 
except Exception as e:
    print("something went to wrong..",e)  

finally:
    print("resource is closed")
              


