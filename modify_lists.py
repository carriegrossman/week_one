han_description = ['stuck up', 'half-witted', 'scruffy-looking', 'nerf herder']
print(han_description)

han_description[2] = "Who's scrffy looking?"
han_description[3] = "Master Pilot"
print(han_description)
#This replaces an item in a list


falcon_parts = ["Toplex Deflector Shield", "V-5 Navigation Computer", "YT-1300 Hyperdrive", "AG-26 Laser Cannon", "Escape Pod"]
print(falcon_parts)

hans_modifications = ["L3 + V-5 Navigation", "SSP05 Hyperdrive"]
print(falcon_parts[1:3])
#Prints the modifications and replaces the og
#if you print(falcons_parts[1])/single index it will take the whole list and insert it into the other list

falcon_parts[1:3] = hans_modifications
print(falcon_parts)

#start here for below
falcon_parts = ["Toplex Deflector Shield", "V-5 Navigation Computer", "YT-1300 Hyperdrive", "AG-26 Laser Cannon", "Escape Pod"]
print(falcon_parts)

del falcon_parts[-1]
print(falcon_parts)
#delete an item

falcon_parts.append("AG-26 Laser Cannon")
print(falcon_parts)
#this adds an item to the end of the list

falcon_parts.extend(["Sensor Proof Smuggler Compartment", 'Aurodium Gold Dice'])
print(falcon_parts)
#adds a list to a list

falcon_parts.insert(0, "Dejarik Board")
print(falcon_parts)
#this inserts the item and shifts the items down the list and does not replace the items

falcon_parts =[
    "Toplex Deflector Shield", 
    "V-5 Navigation Computer", 
    "YT-1300 Hyperdrive", 
    "AG-26 Laser Cannon", 
    "Escape Pod"
]
print(falcon_parts)
#will still print in a line

poorly_cloned_falcon = falcon_parts + ["Wookie"]
print(falcon_parts)
print(poorly_cloned_falcon)
#This adds the list(falcon_parts and wookie) to poorly_cloned_falcon

removed_part = falcon_parts.pop(7)
print(removed_part)
print(falcon_parts)
#this states what item you removed or pop
#pop with out a number(agruement removes the last item)