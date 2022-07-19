import random 

x=random.randint(1,100)
for i in range(5):
    n=int(input("enter a number:"))
    if n==x:
        print("you guessed it:",x)
        break
    elif x<n:
        print("your value is higher than x")
    elif x>n:
        print("your value is lower than x")
    if i==4:
        print("you lose:",x)

