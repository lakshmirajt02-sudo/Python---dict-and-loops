# lambda function / anonymous function
# no def keyword, instead lambda keyword

# variable = lambda arguments : expression/statements 
# add = lambda a , b : a + b
# print(add(10 , 5))

#square
# n = 8 
# square = lambda x : x * x
# print(square(n))

# map() -  needs 2 arguments 
# numbers = [1, 2, 3, 4, 5]
# new_list = map(fun, list)
# new_list = list(map(lambda r : r * 2, numbers))
# print(new_list)

# fruits = ['mango', 'kiwi', 'avocado']
# new_fruit = list(map(lambda itm : itm + ' fruit', fruits))
# print(new_fruit)

# filter() 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# new_list = list(filter(lambda num : num > 4, numbers))
# print(new_list)

# even_list = list(filter(lambda num : num % 2 == 0 , numbers))
# print(even_list)

# reduce()
from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# result = reduce(lambda x , y : x + y , numbers)
# print(result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
filtered_list =  list(filter(lambda itm : itm % 2 == 0, numbers))
even_sum  = reduce(lambda a, b : a + b, filtered_list)
print(even_sum)



