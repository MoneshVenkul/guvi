
class main():
    def func(self,a,b):
       for i in range (a,b):
            if (i%2!=0):
                print(i,end=" ")
ob = main()
a,b = input().split()
a = int(a)+1
b = int(b)
ob.func(a,b)
