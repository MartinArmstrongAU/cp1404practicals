COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}

colour_name = input("Please enter a colour: ")
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print("The code for {} is {}".format(colour_name, COLOUR_CODES[colour_name]))
    else:
        print("That is an invalid name. Please try again.")
    colour_name = input("Please enter a colour: ")
