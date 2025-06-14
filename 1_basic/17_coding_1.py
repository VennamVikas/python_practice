#write a program to find out how many days,weeks and months we have left in if we live 90 years old

current_age=int(input("Enter age :"))

years_left=90-current_age

days=years_left * 365
weeks= years_left * 52
months= years_left * 12

print(f"you have {days} days,{weeks} weeks and {months}months left to 90 years")



