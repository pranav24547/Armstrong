a=input("Enter first string:-") 
b=input("Enter second string:-")
c=[]
d=[]
for i in a:
    c.append(i)
c.sort()
for i in b:
    d.append(i)
d.sort()
if c == d:
    print("Its an anagram")
else:
    print("Its not an anagram")