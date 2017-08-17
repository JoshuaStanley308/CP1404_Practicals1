
def main():

    name = get_name()
    frequency_of_letters = int(input("Frequency of letters: "))

    print_name(name, frequency_of_letters)


def print_name(name, frequency_of_letters):
    print(name[::frequency_of_letters])


def get_name():
    name = input("Please enter your name: ")
    while len(name) == 0:
        print("error, cannot leave it blank")
        name = input("Please enter your name: ")
    return name

main()
