
print("Please enter your name: ")
name = input("> ")
while len(name) == 0:
    print("error, cannot leave it blank")
    print("Please enter your name: ")
    name = input("> ")
print(name[0:len(name):2])
