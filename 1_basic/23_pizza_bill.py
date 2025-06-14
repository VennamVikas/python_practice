#pizza bill for small pizza Rs:100, Medium pizza Rs:200 and Large pizza Rs 300
# for extra cheese for any size pizza = 20
# pepperoni for small pizza =30
# pepperoni for medium + large =50  

size=input("What size pizza do you want(S/M/L)?:")

bill=0
if(size=='S' or size=='s'):
    bill=100
    print("Small pizza is 100 Rs.")
elif(size=='M' or size=='m'):
    bill=200
    print("Small pizza is 200 Rs.")
else:
    bill=300
    print("Small pizza is 300 Rs.")

add_pepper=input("Do you want pepperoni (Y/N)?")
if(add_pepper=='Y' or add_pepper=='y'):
    if(size=='S' or size=='s'):
        bill+=30
    else:
        bill+=50

extra_chesse=input("Do you want extra cheese(Y/N)?:")
if(extra_chesse=='Y' or extra_chesse=='y'):
    bill+=20

print(f"Your Total bill is {bill}")