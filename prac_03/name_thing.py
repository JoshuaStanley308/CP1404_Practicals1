
def main():
    print("Please enter your name: ")
    name = input("> ")
    frequency_of_letters = int(input("Frequency of letters: "))
    name = get_name(name)
    print_name(name, frequency_of_letters)


def print_name(name, frequency_of_letters):
    length_of_name = len(name)
    print(name[0:length_of_name:frequency_of_letters])


def get_name(name):
    while len(name) == 0:
        print("error, cannot leave it blank")
        print("Please enter your name: ")
        name = input("> ")
    return name

main()
