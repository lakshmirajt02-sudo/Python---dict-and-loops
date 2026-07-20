# sqaure pattern 
for i in range(5):
   for j in range(5):
      print("*" , end="  ")
   print()

# rectangle pattern 
for i in range(6):
   for j in range(5):
      print("*" , end="  ")
   print() 
   
# inverted triangle   
for x in range(5 , 0 , -1):
   for y in range(x):
      print("*", end = " ")
   print()

# right triangle    
for a in range(6):
   for b in range(a):
      print("*", end=" ")
   print()
   
# number triangle 
for e in range(1 , 6):
   for f in range(1 , e+1):
      print(f , end=" ")
   print()
   
# floyd's triangle 
num = 1
for g in range(1, 5):
   for h in range(g):
      print(num, end=" ")
      num += 1
   print()
   
# alphabet pattern 
for k in range(5):
   for l in range(k+1):
      print(chr(65 + l), end = " ")
   print()
   
# pyramid pattern
for s in range(5):
   print(" " *(5-s-1), end=" ")
   for t in range(s + 1):
      print("*", end=" ")
   print()
