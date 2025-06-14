#WAP to check the roller coaster token  

height= int(input("what is your height in feets:"))

if(height >= 3 and height <=15):
    print("you can ride")
    age=int(input("what is your age :"))
    if(age <=12 ):
        print("pay Rs:150")
    elif(age <=18 ):
        print("pay Rs:250")
    else:
        print("pay Rs:500")
else:
    print("can't ride")
print("BYE BYE")