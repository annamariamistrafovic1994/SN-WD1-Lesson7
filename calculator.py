x = int(input("unesi prvi broj: "))
print(x)

y = int(input("unesi drugi broj: "))
print(y)


o = input("za operaciju y od x unesi 1, za obratno unesi 2: ")
print(o)

operation = input("unesi operaciju (+, -, /, *): ")
print(operation)

if operation == "-":
    o = input("za operaciju y od x unesi 1, za obratno unesi 2: ")
    print(o)
if operation == "+":
    print(x+y)
elif operation == "-":
    if o == "1":
       print(x-y)
    if o == "2":
       print(y-x)
elif operation == "/":
    print(x/y)
elif operation == "*":
    print(x*y)
else:
    print("Nije ispravan operator!")
