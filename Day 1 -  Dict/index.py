# before python 3.7 version - unordered 
# after 3.7 version - ordered 

# my_dict = {
#    'name' : 'Lakshmi',
#    'age' : 23 ,
#    'city' : 'calicut'
# }
# print(my_dict)

# creating dictionaries 
# my_dict = {'name': 'lakshmi', 'age': 23, 'city': 'calicut'}
# empty_dict = {}
# from_keys = dict.fromkeys(['a', 'b'])

# my_dict = {
#    'name' : 'Lakshmi',
#    'age' : 23 ,
#    'city' : 'calicut',
#    'name' : 'Panchami'
# }
# print(my_dict) #can create duplicate key but the second one overides it
# print(my_dict['name'])
# print(my_dict['age'])
# print(my_dict['city'])

# Dictionary Methods 
# ------------------
# my_dict = {
#    'name' : 'Lakshmi',
#    'age' : 23 ,
#    'city' : 'calicut',
#    'is_Active': True
# }

# keys() - get all keys 
# print(my_dict.keys())
# print(type(my_dict.keys()))

# values() - get all values 
# print(my_dict.values())

# items() - get key-value pairs 
# print(my_dict.items())    #tuple inside list

# get(key, default) - safely get value
# print(my_dict.get('rollno', 0))

# pop() - remove and return value
# print(my_dict.pop("city")) 
# print(my_dict) 

# update(dict2) -  merge dictionaries 
# dict1 = {'a' : 1 , 'b' : 2}
# dict2 = {'c' : 3 , 'd' : 4}
# dict1.update(dict2)
# print(dict1)

# clear() - remove all items 
# dict1.clear()
# print(dict1)

# copy() - create shallow copy
# dict2 = {'c' : 3 , 'd' : 4}
# new_copy = dict2.copy()
# print(new_copy)






