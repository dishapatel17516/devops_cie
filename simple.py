p = int(input("enter percentage"))
t = int(input("enter time"))
r = int(input("enter rate"))

SI = (p*t*r)/100
print("Simple Interest: ",+SI)

amount = p*(1+r/100)**t 
ci = amount - p
print("Compound Interest :", +ci)

print("this end of the program")
