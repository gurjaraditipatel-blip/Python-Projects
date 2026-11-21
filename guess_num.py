import random


computer=random.randint(1,100)
n=-1
guesses=0
while(computer!=n):
   n=int(input("Enter your number:"))
   guesses+=1
   if(computer==n):
     print("you win\nGame Over!!")
     break
   elif(computer>n):
     print("guess the greater number")
   else:
     print("guess lower number")

print(f"you have guess the no correctly in {guesses} attempts")