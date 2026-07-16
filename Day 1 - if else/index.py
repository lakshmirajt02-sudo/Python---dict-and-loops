# if 
# if True:
#    print("Hello python")
#    print("Hello C")
#    print("Hello java")
#    print("Hello javascript")
#    print("Hello C++")

# if else    
# number = 10
# if number > 0 :
#    print(f'{number} is positive')
# else : 
#    print(f'{number} is negative')
   
# if..elif..else
number =  0   
if number > 0 :
   print('Positive number')
elif number < 0 :
   print('Negative number')
elif number == 0 :
   print('Number is zero')
else: 
   print(number,"is not a number")
   
num = int(input('Enter a number: '))
if num % 2 == 0:
   print(num,' is even number')
else:
   print(num, 'is odd')
   
# nested if  
age = int(input('Enter age:'))
has_license = True
if age >= 18:
   if has_license :
      print('You can drive')
   else:
      print('You cannot drive')
else:
   print('You are underage')
