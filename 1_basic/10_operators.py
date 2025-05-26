#arithimatic operators 

print(10/2)
print(10//2) # flowdevision

print("Remider :",10%2)
print("Remider :",5%2)

print(5 + 2 * 3 - 1 + 10 / 5)


#calculate_BMI
#weight/(height *height)
a=input("enter the weight in kg's :")
b=input("enter the weight in meters :")

weight= int(a)
height= float(b)
print("BMI :",weight/(height*height))



#assignment operators
print("Assignment operators")
x=6
y=6

x+=2
y-=2
print("x= ",x)
print("y= ",y)

#comparision operators
z=8
print("comparision operators")
print((z==5))
print(z<=5)
print(z>=5)
print(z!=8)

#logical operators
#(and)  (or) (not)
print("logical operators :")
print(z<5 and z==5)
print(z<5 and z==8)
print(z<5 or z==8)
print(z<5 or z==5)
print("Not :",not(z))