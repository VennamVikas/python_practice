
year=int(input("enter year :"))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")     
else:
    print("Not a leap year not div by 4")
