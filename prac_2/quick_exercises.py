out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is {}".format(name))
in_file.close()

in_file = open("numbers", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
total = number_1 + number_2
print(total)
in_file.close()
