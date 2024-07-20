list = ["Red", "Blue"]
#Add one item to list
list.append("White")
print(list)

#Add list to list
list.extend(["Yellow","Green"])
print(list)

#Add to index
list.insert(2,"Teal")
print(list)

#Remove By item
list.remove("Yellow")
print(list)

#Remove on Giving index
list.pop(1)
print(list)

#Delete by index
del list[2]
print(list)
# del list[startIndex,number_del]
del list[0:3]
print(list)
#del all
del list[:]
print(list)
#clear all data
list.clear()
print(list)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#count fruit
count_f=fruits.count('apple')
print(count_f)
#Reverse fruit
fruits.reverse()
print(fruits)
#Sort fruit
fruits.sort()
print(fruits)
