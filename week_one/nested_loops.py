#string and lists
giant_exogorth = [
    "Millennium Falcon",
    ['mynock 1', 'mynock 2', 'mynock 3'],
    ['parasite exogorth', 'parasite exogorth 2']
]

print(giant_exogorth[1])
#item 1 is the ENTIRE list within the list

#assign indexed item to a variable
mynocks = (giant_exogorth[1])
#this would print mynock 2
print(mynocks)
#---------------------------
print(giant_exogorth[1][0])
#we want item in index 1 and then the 0 item in the index - mynock1
print(giant_exogorth[2][1])
#this prints out parasite exogorth 2


#you can loop through a nested list within another nested list

#tuple

my_tuple = (1, 2, 3)
print(my_tuple [0])
#you use () instead of [] 
#once you declare a tuple you can not change that
