def main():
    score = get_score()
    print(determine_grade(score))


def determine_grade(score):
    if score < 0 or score > 100:
        final_grade = "Invalid score"
    elif score < 50:
        final_grade = "Bad"
    elif score >= 90:
        final_grade = "Excellent"
    else:
        final_grade = "Passable"
    return final_grade


def get_score():
    score = float(input("Enter score: "))
    return score


main()
