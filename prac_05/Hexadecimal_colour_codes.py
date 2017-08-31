colour_codes = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine1": "#7fffd4",
                "azure1": "#f0ffff", "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000",
                "blanchedalmond": "#ffebcd", "blue1": "#0000ff", "blueviolet": "#8a2be2"}

colour = input("Enter colour name: ").lower()
while colour != "":
    if colour in colour_codes:
        print(colour, "is", colour_codes[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ").lower()
