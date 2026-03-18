def change_coords(x1, y1, x2, y2, dict):
    dict["coords"] = [[x1, y1], [x2, y2]]
    dict["width"] = abs(x1 - x2)
    dict["height"] = abs(y1 - y2)
    return dict

# figures = [
#     {"width" : 7, "height" : 6, "color" : "blue", "coords" : [[0, 6], [7, 0]]},
#     {"width" : 10, "height" : 5, "color" : "blue", "coords" : [[0, 5], [10, 0]]}
# ]

rectangle = {"width" : 7, "height" : 6,
             "color" : "blue", "coords" : [[0, 6], [7, 0]]}

# for figure in figures:
#     print(figure["coords"])
rectangle2 = change_coords(1, 7, 4, 4, rectangle)
print(rectangle)
print(rectangle2)