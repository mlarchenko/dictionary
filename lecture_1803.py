rectangle = {"width" : 7, "height" : 6,
             "color" : "blue", "coords" : [[0, 6], [7, 0]]}
print(rectangle["height"])
print(rectangle["coords"][1])
print(rectangle.get("width"))
print(rectangle.get("area"))
if rectangle.get("area") == None:
    rectangle["area"] = rectangle["width"]*rectangle["height"]
print(rectangle["area"])
#квадратні дужки coords[][] для списку в списку
print(rectangle)



