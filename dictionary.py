# #simple Key (left) Values/Items (right)

#1
# fruits_and_colors = {
#     "Apples":"red",
#     "Orange":"orange",
#     "Lemon":"yellow",
#     "Grapes":"purple"
# }
# print(fruits_and_colors)

#2
# force_side = {
#     "Light": ["Luke", "Yoda"],
#     "Dark": ["Maul"],
#     "Grey": ["Han"]
# }
# print(force_side["Light"])
# #we access items by its key

#3
# force_side = {
#     "Light": ["Luke", "Yoda"],
#     "Dark": ["Maul"],
#     "Grey": ["Han"]
# }
# print(force_side["Light"][0])
#OR
# light_side = force_side["Light"]
# print(light_side[1])

#4 print within the 2nd dict.
# Colors = {
#     "Red" : ['Apple', 'Cherry'],
#     "Orange": "Orange",
#     "More": {
#         "Yellow" : ['Lemon', 'Banana', 'Mango']
#     },
#     "Green" : ['Kiwi', 'Lime']
# }
# more = Colors["More"]
# print(more)

#5 adding to the dictionary
# Colors = {
#     "Red" : ['Apple', 'Cherry'],
#     "Orange": "Orange",
#     "More": {
#         "Yellow" : ['Lemon', 'Banana', 'Mango']
#     },
#     "Green" : ['Kiwi', 'Lime']
# }

# Colors["More"]["Vegetables"] = ["Squash", "Corn"]
# print(Colors["More"])
# #replacing the values instead a list.
# Colors["More"]["Vegetables"] = "All yellow"
# print(Colors["More"])

#6 deleting a
# Colors = {
#     "Red" : ['Apple', 'Cherry'],
#     "Orange": "Orange",
#     "More": {
#         "Yellow" : ['Lemon', 'Banana', 'Mango']
#     },
#     "Green" : ['Kiwi', 'Lime']
# }
# del Colors["Green"]
# print(Colors)

#7 
# Colors = {
#     "Red" : ['Apple', 'Cherry'],
#     "Orange": "Orange",
#     "More": {
#         "Yellow" : ['Lemon', 'Banana', 'Mango']
#     },
#     "Green" : ['Kiwi', 'Lime']
# }
# #see if key is in dict.

# # if "Purple" in Colors:
# #     print("yum")
# # else: 
# #     print('No purple here')

# if "More" in Colors:
#     print("Yum")
# else:
#     print("No more")


#8 
colors = {
#     "Red" : ['Apple', 'Cherry', 'Strawberry'],
#     "Orange": "Orange",
#     "More": {
#         "Yellow" : ['Lemon', 'Banana', 'Mango']
#     },
#     "Green" : ['Kiwi', 'Lime']
# }
#print out the keys only and doesnt go inside
# for key in colors:
#     print(key)

#this prints out the values only
# for key in colors:
#     print(colors[key])
    
#9 this is adding to the 
# colors = {
#     "Red" : ['Apple', 'Cherry', 'Strawberry'],
#     "Orange": "Orange",
#     "More": {
#         "Yellow" : ['Lemon', 'Banana', 'Mango']
#     },
#     "Green" : ['Kiwi', 'Lime']
# }
# more = colors["More"]
# print(more)
# more["Purple"] = "Grapes"
# print(more)

# print(colors)