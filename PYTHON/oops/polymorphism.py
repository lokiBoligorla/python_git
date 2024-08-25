
#Duck typing in polymorphism
# class Pycharm:
#     def execute(self):
#         print("compiling")
#         print("output")
# class MYeditor:
#     def execute(self):
#         print("compiling")
#         print("output")
#         print("debugging")
#         print("spell check")

# class laptop:
#     def code(self,ide):
#         ide.execute()
# lap1=laptop()
# p1=Pycharm()
# m1=MYeditor()
# lap1.code(p1)
# lap1.code(m1)

#operator overriding
# class student:
#     def __init__(self,m1,m2):
#           self.m1=m1
#           self.m2=m2
#           print(m1,m2)
#     def __add__(self,other):
#          m1=self.m1+other.m1 
#          m2=self.m2+other.m2 
#          s3=student(m1,m2)
#          return s3 
#     def __sub__(self,other):
#         m1=self.m1-other.m1 
#         m2=self.m2-other.m2 
#         s4=student(m1,m2)
#         return s4
#     def __gt__(self,other):
#          r1=self.m1+self.m2
#          r2=other.m1+other.m2
#          if r1>r2:
#               return True
#          else:
#               return False
#     def __str__(self):
#          return self.m1,self.m2     
            
# s1=student(100,100)
# s2=student(70,10)
# s3=s1+s2
# s4=s1-s2
# print("addition",s3.__str__())
# print("subtraction",s4.__str__())
# if s1 > s2:
#      print("s1 wins")

# else:
#      print("s2 wins")   



#Method overloading   
# class student:
#      def sum(self,a=0,b=0,c=0): #method overloading== In a class we have multiple method with the same name but
#                                                       # But,different in the number of passing arguments 
#          return a+b+c
#      def sum(self,a=0,b=0,c=0,d=0):
#          return a+b+c+d
# s1=student()
# print(s1.sum(2))
# print(s1.sum(2,3))
# print(s1.sum(6,7,8))
# print(s1.sum(4,5,6,4))  



#another approach to find the method overloading
# class student:
#      def sum(self,a=None,b=None,c=None):
#          if a!=None and b!=None and c!=None:
#               print(a+b+c)
              
#          elif a!=None and b!=None:
#               print(a+b)
#          else:
#              print(a)
          
# s1=student()
# s1.sum(2)
# s1.sum(2,3)
# s1.sum(2,3,4)          


#Method overriding

class A:               
    def show(self):
        print("in A")
class B(A):
    def show(self):
      
        print("in B") 
     

b=B()
b.show()       
            