a=int(input("Enter an number:-"))
value=0
for i in range(2,a):
    if a%i==0:
        value=1

if value==1:
    print(a,"is not an prime number")
else:
    print(a,"is a prime number")