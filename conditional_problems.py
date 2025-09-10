#wap to check if a number is positive or negative
x = float(input("Enter the number: "))
print("The Given Number is Positive") if x>=0 else print("The Given Number is Negative")

#wap to check whether a number is positive or negative
y = int(input("Enter your Number=> "))
print("Given Number Is Even") if y%2 ==0 else print("Given Number Is Odd")

# wap to create a simple area calculator
print("WELCOME TO AREA CAlCULATOR!")
print("Press 1 to calculate area of square")
print("Press 2 to calculate area of rectangle")
print("Press 3 to calculate area of circle")
print("Press 4 to calculate area of triangle")

choice = int(input("Pick a number to calculate area of your desired geometry: "))

if choice == 1 :
    side = float(input("enter side of the square: "))
    area1 = side**2
    print("Area of the square is: ", area1)

if choice==2 :
    l = float(input("enter length of the rectangle: "))
    b = float(input("enter breadth of the rectangle: "))
    area2 = l*b
    print("Area of rectangle is :" , area2)

if choice==3 :
    r = float(input("enter radius of circle: "))
    area3 = 3.14*r*r
    print("Area of circle is: " , area3)

if choice==4 :
    h = float(input("Enter height of the triangle: "))
    base = float(input("enter base of the triangle: "))
    area4 = 1/2*h*base
    print("Area of the triangle is: " , area4)

print("THANK YOU FOR USING OUR AREA CALCULATOR!")

# #wap to check whether passed letter is vowel or not
letter = input("enter the letter: ")
if (letter in "aeiou") or (letter in "AEIOU") :
    print("it is a vowel")
else: 
    print("it is a consonant")

#wap to check if a number is single digit 2 digit and so on ... till 5 digit number
num = int(input("enter your number upto five digit: "))

if num>=0 and num<=9 :
    print("it is single digit number")

elif num>=10 and num<=99:
    print("it is two digit number")

elif num>99 and num<=999 :
    print("it is a three digit number")
 
elif num>=1000 and num<=9999 :
    print("it is four digit number")

elif num>=10000 and num<=99999 :
    print("it is five digit number")





