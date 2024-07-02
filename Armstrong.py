n=int(input("Enter the length of the list:"))
ans=0
for i in range(n): 
    Number=int(input())
    Numstr=str(Number)
    length=len(Numstr)
    sum=0
    for i in Numstr:
        #1,5,3
        sum +=int(i)**length
    if sum == Number:
        ans +=1
print(ans)