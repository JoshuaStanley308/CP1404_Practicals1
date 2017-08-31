

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invlaid score")
elif score < 50:
    print("Bad")
elif score >= 90:
    print("Excellent")
else:
    print("Passable")

