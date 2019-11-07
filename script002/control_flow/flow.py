a = 10
PEP8

if a > 15: print("more than 15")

a = "111"
if a:
    a = a * 2
    if len(a) == 6:
        print(a)


a = 3
if a < 5:
    print("less than 5")
elif a > 5 and a <= 10:
    print("more than 10")

elif a > 10 and a <= 15:
    print("more than 10")
# elif a > 11 and a < 13:
#     print("more than 10")
else:
    print("more than 15")

a = 0
while True:
    print(a)
    a += 1
    if a == 4: break
else:
    print("non-broken exit!")


for x in "non-empty string!":
    if x == '-': continue
    print(x, end="")
    if x == "!": break
else:
    print("non-broken exit from for loop")


for element in range(1, 5): print(element)

for element in range(0, 5, 2): print(element)



# range, enumerate

for x in range(5):
    print(x)

for position, element in enumerate("string", start=1):
    print(f"position is {position}, element is {element}")