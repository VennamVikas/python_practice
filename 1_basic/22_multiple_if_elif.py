#WAP to check the roller coaster token

#variable 1
height= int(input("what is your height in feets:"))
#variable 2
bill=0

if(height >= 3 and height <=15):
    print("You can ride")
    #variable 3
    age=int(input("What is your age :"))

    if(age <=12 ):
        bill=150
        print("Ticket price is Rs:150")
    elif(age <=18 ):
        bill=150
        print("Ticket price is Rs:250")
    else:
        bill=150
        print("Ticket price is Rs:500")
    
    #variable 4
    want_photo=input("Do you want to take photo(Y/N):")
    if(want_photo == 'y' or want_photo == 'Y'):
        bill=bill+50
    print(f"Your total bill is {bill}")
else:
    print("Can't ride")
print("BYE BYE")