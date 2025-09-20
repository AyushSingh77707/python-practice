#problem1: wap to find sum of all even number up to 50
#method 1
sum = 0
for i in range(2,51,2):
    sum+=i
print("the sum of all even numbers upto 50 is:", sum)

#method 2
sum = 0
for i in range(1,51):
    if i%2 == 0 :
        sum+=i
print("the sum of even numbers upto 50 is:", sum)

#problem2:wap to write first 20 numbers and their square numbers

for i in range(1,21):
    print(i,"=>",i**2)

#problem3:wap to find sum of first 10 odd numbers using while loop

n=0
sum=0
while n<=20:
    if n%2!=0 :
        sum+=n
        n+=1
        
print("the sum of first 10 odd numbers is:" , sum)

#problem4:wap to check if a number is divisible by 8 and 12 upto 100 numbers

for i in range (1,101):
    if i%8 == 0 and i%12 == 0 :
        print(i)

#problem5: wap to create a billing system at supermarket

while True:
    n= input("Enter Customer name=>")
    a= 0

    while True:
     q = int(input("Enter the quantity=>"))
     p = float(input("Enter the price=>"))
     a += q*p

     r = input("want to add more items, Yes/no: ")
     if r == "no" or r == "No":
        break
    

    print("*"*100)
    print("NAME:", n)
    print("Total Amount to be Paid=>" , a)
    print("*"*100)
    print("happy shopping!")

    i = input("do you want to go to next customer? (yes/no): ")
    if i == "no" and i == "No" :
     break



#fibonacci series==> third number is sum of preceeding two numbers starts from 0 , 1 , 1, 2 , 3 , 5 ......
a = 0
b = 1
n = int(input("Enter the number till you want your fibbonaci series: "))
if n == 1 :
   print(1)
else:
   print(a) 
   print(b)
for i in range (2,n):
   c = a+b
   a = b
   b = c
   print(c)

#write a programm to check whether a number is prime or not
num = int(input("enter your digit: "))
if num<=1: print("It is not a prime number")
else:
   for i in range(2,num):
      if num%i == 0 : print("it is not a prime number")
      else: 
         print("It is a prime number")
         
#palindrome program using string slicing
s= input("Enter your object: ")
rev = s[::-1]
print("It is palindrome") if s == rev else print("It is not palindrome")

#palindrome numbers using loops and conditional statement

num = int(input("Enter your number: "))
temp = num
rev = 0
while num>0:
  digit=num%10
  rev = rev*10 + digit
  num = num//10

if rev == temp:
   print("it is palindrome number")
else :
   print("it is not palindrome")







    

    



        
