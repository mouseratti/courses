a = 10


if a > 15: print("more than 15")


if a > 5:
    print("more than 5")
elif a > 10 and a < 15:
    print("more than 10")
else:
    print("more than 15")




a = 0

while a < 5:
    print(a)
    a += 1
    # if a = 4: break
else:
    print("non-broken exit!")


for x in "non-empty string!":
    print(x)
    if x == ' ': continue
    if x == "!": break
else:
    print("non-broken exit from for loop")


