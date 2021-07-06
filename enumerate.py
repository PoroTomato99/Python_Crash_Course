def skip_elements(elements):
	# code goes here
	new_list = []

	for index, item in enumerate(elements):
		if index % 2 == 0:
			new_list.append(item)
			print(f"{index} ::: {item}")
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) 
# Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) 
# Should be ['Orange', 'Strawberry', 'Peach']