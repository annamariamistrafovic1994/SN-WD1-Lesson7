x = input("What mood are you in? ")
print(x)

operation = input("Choose one of the given solutions (happy, sad, relaxed, nervous, excited): ")
print(operation)

if operation == "happy":
    print("It is great to see you happy!")
elif operation == "sad":
    print("Cheer up!")
elif operation == "relaxed":
    print("Stay in ZEN.")
elif operation == "nervous":
    print("Take a deep breath 3 times.")
elif operation == "excited":
    print("Keep the adrenaline up!")
else:
    print("I don't recognize this mood.")