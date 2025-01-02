def colour_trio(colours):
    nextColors = {
        "yy": "y",
        "rr": "r",
        "bb": "b",
        "yr": "b",
        "ry": "b",
        "by": "r",
        "yb": "r",
        "rb": "y",
        "br": "y"
    }
    while len(colours) > 1:
        newColours = ""
        for i in range(len(colours) - 1):
            newColours += nextColors[colours[i]+colours[i+1]]
        colours = newColours
    return colours
w

print(colour_trio("rybyry"))