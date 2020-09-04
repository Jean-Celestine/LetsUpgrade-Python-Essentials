#Program - 1 [Giving instruction to pilot according to altitude]
height = int(input("Enter Height : "))

if (height<=1000):
    print("Safe to land!")

elif (height>=1000 and height<5000):
    print("Bring down to 1000")
else:
    print("Turn Around and try later")



#Program - 2 [Printing prime numbers]
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num) 
