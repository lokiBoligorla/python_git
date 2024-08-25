# class A:
#     def feature1(self):
#         print("from feature1")
#     def feature2(self):
#         print("from feature2")    
# class B(A):#B class is derived from class A =====single-level inheritence
#     def feature3(self):
#         print("from feature3")
#     def feature4(self):
#         print("from feature4")

# class C(B):#C class is derived from the class B =====multi-level inheritance
#     def feature5(self):
#         print("from feature5")  

# class D(A,B,C):#D class ia derived from the class A,B,C ===== multiple inheritance
#     def feature5(self):
#         print("from feature5")              
# a=A()
# b=B()
# c=C()
# d=D()

# a.feature2()
# a.feature1()

# d.feature1()
# d.feature2()
# d.feature3()
# d.feature4()
# d.feature5()



class A:
    def __init__(self):
        print("A init method")

    def feature1(self):
        print("A this is from feature1")
    def feature2(self):
        print("A this is from feature2")    
class B(A):
    def __init__(self):
        super().__init__()
        print("B init method")

    def feature1(self):  
         super().feature1()             
         print("B this is from feature1")
    def feature2(self):
        super().feature2()
        print("B this is from feature2") 



b=B()

b.feature1()
b.feature2()







