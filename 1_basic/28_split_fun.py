import random
#text=input("enter your names:")
text="vikas senu anu manu"
print(text)
splited_text= text.split(" ")
print(splited_text)
l=len(splited_text)
print(l)
r=random.randrange(0,l)
print(r)
print(f"{splited_text[r]} will pay the bill...")

#simple way using choice_fun
names="vikas senu anu manu"
splited_names= names.split(" ")
select_name=random.choice(splited_names)
print(f"{select_name} will pay the bill...")

