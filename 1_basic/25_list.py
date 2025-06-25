num= [10, 0, -1, 7, 20, 30]
name=["vikas","senu","anu","manu"]
mix_list=["vikas",1,"senu",10.0]


print("lenth :",len(num))

print(num[0])
print(name[1])
print(num[1:4])

#num.sort() #sorting

num.append(60)            # the number will add end of the list
num.insert(1,45)          #the number will add in index place
num.extend([66,67,68,69]) #add the multiple numbers at a time



#num.remove(0)              #fist accurence of number will removed from the list 
num.pop(6)
print(num)

