my_dict = {"Максим" : 1999 , "Лилия" : 1998 , "Дима": 1994}
print(my_dict)
print(my_dict.get("Дима"))
print(my_dict.get("Вася"))
my_dict.update({"Лера" : 2000 , "Саша" : 2001})
a = my_dict.pop("Дима")
print(a)
print(my_dict)
my_set = {1, 1 , "Type" , (3), (3) , "Type"}
print(my_set)
my_set.add(4)
my_set.add("SSS")
my_set.discard(1)
print(my_set)