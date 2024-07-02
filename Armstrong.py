Number=int(input("Enter the number:"))
Numstr=str(Number)
length=len(Numstr)
sum=0
for i in Numstr:
    sum +=int(i)**length
if sum == Number:
    print(Number,"is an Armstrong Number")
else:
    print(Number,"is not an amstrong Number")



