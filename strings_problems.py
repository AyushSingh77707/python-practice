# Write a programm to seperate following string into coma , seperated values

A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
print(A.split("."))

#write a program to sort strings alphabetically in python

a = input("Enter  the string: ")
b = sorted(a)
print(b)

#write a program to remove a given character from a string
string1 = "Hello World"
print(string1.replace("World" , "Ayush"))

#wap to remove dot(.) from the following string
z = "F.R.I.E.N.D.S"
print(z.replace("." , ""))

#wap to count no of occurence of substring in given string
a = "she sells seashells on the sea shore"
print("the number of occurence of 'sea' is ", a.count("sea"))

#take a input from user as a string , reverse it
s = input("Enter your word here: ")
print(s[::-1])

#wap to check if a string contains only digit
s = input("Enter the string here=>")
if s.isdigit() :
    print("Yes , it contains only digit")
else:
    print("It does not contain only digits")
    
#wap to check a string if it is palindrome or not
pal = input("Enter your word here: ")
lap = pal[::-1]
if pal == lap :
    print("yes it is a palindrome")
else:
    print("it is not a palindrome")
   
#wap to find number of vowels in a string
a = input("enter your sentence here:")
vowel = 0
for i in a:
    if i == "a" or  i == "A" or  i == "e" or  i == "E" or  i == "i" or  i == "I" or  i == "o" or  i == "O" or  i == "u" or i == "U" :
        vowel += 1

print("The number of vowels in given sentence is ",vowel)

#write a program to check if every word in a string begins with capital letter
a = input("enter string here: ")
print(a.istitle())