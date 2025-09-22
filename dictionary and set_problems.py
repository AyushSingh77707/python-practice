#wap to create a dictionary pof hindi words with values a their english transalation.
d = {"khush":"happy","dukh":"sad","gussa":"angry"}
word = input("enter the hindi word you want meaning of:")
print(d[word])

#wap to input eight numbers from user and display all unique number once
s = set()
i= int(input("enter number=>"))
s.add(i)
i= int(input("enter number=>"))
s.add(i)
i= int(input("enter number=>"))
s.add(i)
i= int(input("enter number=>"))
s.add(i)
i= int(input("enter number=>"))
s.add(i)
i= int(input("enter number=>"))
s.add(i)
i= int(input("enter number=>"))
s.add(i)
i= int(input("enter number=>"))
s.add(i)
print(s)

#can we have a set having 18 as integer as well as 18 as a string?
#=>yes becoz they are diffrent data type
a = set()
a.add(18)
a.add("18")
print(a)

#what will be the length of following set s? => 2 bcoz python consider 20=20.0 numerically
'''s = set()
s.add(20)
s.add(20.0)
s.add("20")'''

#s={} what is type of s? 
s={}
print(type(s))

#create an empty dictanory.allow 4 freinds to input their favorite language as value and use key as their name
s = {}
name = input("enter name=>")
lang = input("enter lang=>")
s.update({name:lang})
name = input("enter name=>")
lang = input("enter lang=>")
s.update({name:lang})
name = input("enter name=>")
lang = input("enter lang=>")
s.update({name:lang})
name = input("enter name=>")
lang = input("enter lang=>")
s.update({name:lang})
print(s)

#can you change values of list contained in set s
#s={ 8 , 7 , 9 , "ayush" , [1,2]}
'''not possible becoz set is collection well defined object and it is immutable but the list is
mutable so it doesnt make sense'''
