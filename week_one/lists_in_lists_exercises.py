food_list = [
    ["rice", "seawood", "shrimp"],
    ["strawberry", "blueberry", "grapes"],
    ["cheese", "marinara", "pepperoni"]
]
idx = 0
for food in food_list:
    print("Food #%s has the following ingredients: " % idx)
    for i in food:
        print("    %s" % i)
    idx += 1
