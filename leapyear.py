
year = int(input())
if (year%100==0) and (year%4==0):
    print ("no")
elif (year%100!=0) and (year%4==0):
    print ("yes")
else:
    print ("no")
