# while loop 
n = 5
while n > 0:
   print(n)
   n = n - 1
print("Blastoff!")

# for loop 
# num = [10, 20, 30, 40]
# for i in num:
#    print(i)

# txt = 'John'
# for i in txt:
#    if i == 'h':
#       continue
#       print('h is included')
#       # break
#    else : 
#       print('h is not included')
      
# range  
#-------
# range(start , stop, step)
# for j in range(1,11,2):
#    print(j)

# for i in range(1,11):
#    if i % 2 == 0:
#       print(i ,' is even')

# for i in range(5):
#    print(i)    #output is 0 to 4
   
# for i in range(5, 9):
#    print(i) # o/p 5 to 8 

# # reverse
# for i in range(15, 10, -1):
#    print(i) # o/p 15 to 11 
   
# convert range to list 
# numbers = list(range(1,6))
# print(numbers)

# using range with len() 
# fruits = ['apple', 'banana', 'orange', 'kiwi']
# for i in range(len(fruits)):
#    print(i, fruits[i])

# nested loop 
# for i in range(1,3):
#    print('Outer loop')
#    for j in range(1,3):
#       print('    Inner loop')

# number = int(input('Enter a number: '))
# even = 0
# odd = 0
# for i in range(number):
#    if i % 2 == 0:
#       even = even + i
#    else:
#       odd = odd + i
# print(f"Sum of even numbers is {even} and sum of odd numbers is {odd}")

num  = [10, 2, 3, 4, 5]
sum = 0
for i in range(len(num)):
   sum += num[i]
print(sum)