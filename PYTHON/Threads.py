from threading import *
from time import *
class Hello(Thread):
    def run(self):
         for i in range(5):
              print("Lokesh",i)
              sleep(1.4)
class Hii(Thread):
    def run(self):
         for i in range(5):
              print("Rakesh",i)
              sleep(1.4)
             

h1=Hello()
h2=Hii()
h1.start()
sleep(0.1)
h2.start()
# h1.join()
# h2.join()
print("bye")