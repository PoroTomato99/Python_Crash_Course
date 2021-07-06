wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key in wardrobe:
	for value in wardrobe[key]:
		print("{} {}".format(value, key))