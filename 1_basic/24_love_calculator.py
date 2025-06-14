name1=input("Enter your name:")
name2=input("Enter hir/her name:")

combine_name = name1 + name2
lower_case_name = combine_name.lower()
print(lower_case_name)

t= lower_case_name.count('t')
r= lower_case_name.count('r')
u= lower_case_name.count('u')
e= lower_case_name.count('e')
true= t+r+u+e

l= lower_case_name.count('l')
o= lower_case_name.count('o')
v= lower_case_name.count('v')
e= lower_case_name.count('e')
love= l+o+v+e

score = int(str(true) + str(love))
print(score)