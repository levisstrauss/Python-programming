items = [

("produit1", 10),
("produit2", 9),
("produit3", 12),

]

# Return a list of the prices of the different items
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items ]
print(prices)
#return all item where the price is grether than 10
filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
print(filtered)