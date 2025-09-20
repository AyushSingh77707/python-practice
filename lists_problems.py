a = ["ross" , "rachel" , "monica" , "joe"] 

#wap to swap first and fourth element
a[0],a[3]=a[3],a[0]
print(a)

#wap to add a new value at second position
a.insert(1 , "ayush")
print(a)

#wap to delete a value from third position 
a.pop(2)
print(a)

b = [13 , 7 , 12 , 10]
#wap to multiply all numbers in list
mul = 1
for i in b:
    mul = mul*i

print("the multiplication of the numbers in list is:" , mul)

#wap to get the largest number and smallest no from the list
b.sort()
print("the largest number in list is :" , b[-1])
print("the smallest number in list is :" , b[0])


