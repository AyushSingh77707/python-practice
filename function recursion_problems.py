#wap to find greatest of three numbers using functions
def greatest(a , b , c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    elif c>a and c>b :
        return c
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(greatest(a , b , c))

#wap using function to convert celsius to fahrenheit

def conversion(n):
    temp = ((n*9/5))+32
    return temp

n = float(input("enter temperature in celsius=>"))
print("the temperature in fahrenhiet is", conversion(n),"F")

#write a recursive programm to calculate sum of first n natural numbers

def sum(n):
    return (n*(n+1))/2

n = int(input("Enter the number: "))
print("the sum of first ",n,"natural numbers is =>", sum(n))

#OR

'''
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+4
sum(k)=1 + 2 + 3 ..... + k-1 + k
'''
def sum(k):
    if k==1:
        return 1
    return sum(k-1) + k

k = int(input("enter the number: "))
print("the sum of first",k ,"natural numbers is",sum(k))


#wap to print first n lines of following pattern
'''***********.......n
   **********......(n-1)
   *********.....(n-2)'''
def pattern(n):
    if n==0:
        return ""
    print("*"*n)
    pattern(n-1)

n = int(input("enter the number=>"))
print(pattern(n))

#write a python function which convert inches to cm
def inch_cm(inch):
    return n*2.54

n = float(input("enter the length in inches=>"))
print("the following length in cm is ",inch_cm(n))










