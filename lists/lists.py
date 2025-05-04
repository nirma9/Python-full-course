new_list = [10,20,30,40,50]
fruits = ["apple","banana","orange"]
mixed = [1,"hello",3.14,True]
nested = [1,[2,3],[4,5]]

#access list elements
# print(fruits[0])
# print(fruits[2])
# fruits[1] = "blueberry"
# print(fruits)


#list methods
# print(fruits.pop())
# fruits.append("grapes")
# print(fruits)
# # fruits.remove("orange")
# print(fruits)


# print(len(fruits))
# print(max(new_list))
# print(min(new_list))
# print(sum(new_list))


# #iterations

# for fruit in fruits:
#                print(fruit)

new_list.pop(2)
print(new_list)
fruits.pop(1)
print(fruits)
new_list.remove(40)
print(new_list)

new_list.pop()
print(new_list)
new_list.sort()
print(new_list)

print(dir(new_list))

