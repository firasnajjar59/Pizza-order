print("Small Pizza: 15$")
print("Medium Pizza: 20$")
print("Large Pizza: 25$\n")
print("Pepperoni for small Pizza: +2$")
print("Pepperoni for medium or large Pizza: +3$\n")
print("Extra cheese: +1$")

size=input("What size do want? S,M, or L?")
papperoni=input("Do you want Papperoni? Y or N?")
extra_cheese=input("Do you want Extra cheese? Y or N?")
bill=0
error=False

if size=="S":
    bill=15
elif size=="M":
    bill=20
elif size=="L":
    bill=25
else:
    error=True

if papperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

if extra_cheese=="Y":
    bill+=1
if error:
    print("your input not valid please restart the app")
else:
    print(f"Your final bill is {bill}$")