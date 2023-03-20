import random
a=input("Enter 0=rock ; 1=paper ; 2=scissors :\n ")
b=random.randint(1,3)
print("computer choice :",b)

if a==0 and b==0:
      print("even")
elif a==0 and b==1:
      print("you lose!")
elif a==0 and b==2:
      print("you win!")


if a==1 and b==1:
      print("even")
elif a==1 and b==2:
      print("you lose!")
elif a==1 and b==0:
      print("you win!")

if a==2 and b==2:
      print("even")
elif a==2 and b==0:
      print("you lose!")
elif a==2 and b==1:
      print("you win!")
