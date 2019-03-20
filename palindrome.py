
a = int(input())
temp = a
sum = 0
while (a!=0):
    r = a%10
    sum = (sum*10)+r
    a = (a//10)
if (sum == temp):
    print ("yes")
else:
    print ("no")
