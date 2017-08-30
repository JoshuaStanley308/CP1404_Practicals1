import random

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_picks = []
    for j in range(1, 7):
        random_number = random.randint(1, 45)
        while random_number not in quick_picks:
            quick_picks.append(random_number)
            quick_picks.sort()
    print(quick_picks)

