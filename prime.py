
# Python program to check if the input number is prime or not

num = 407

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print("no")
           break
   else:
       print("yes")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print("no")
