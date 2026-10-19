fruit = ["apple"]
fruit.append("grapes")
fruit.insert(0,"Papaya")
fruit.extend(["Mango"])
fr = ['Litchi','dragonfruit','kiwi']
fruit = fruit+fr
print(len(fruit))
print(fruit)
print(fruit[2])
print(fruit[-2])
print(fruit.pop())
print(fruit)
l = [1,2,5,3,5,3,6,4,6,3,1,3,4,8,9,5,8,9,7,7,3,2,2,1]
print(len(l))  
l.reverse()
print(l)