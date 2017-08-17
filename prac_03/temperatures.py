"""
CP1404 / CP5632 - Practical
Pseudocode for temperature converson
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = float(input("Celsius: "))
            print("Result: {:.2f} F".format(c_to_f(fahrenheit)))
        elif choice == "F":
            celsius = float(input("Fahrenheit: "))
            print("Result: {:.2f} C".format(f_to_c(celsius)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


def f_to_c(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def c_to_f(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()

