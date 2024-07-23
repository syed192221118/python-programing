tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
element_to_search = 3

concatenated_tuple = tuple1 + tuple2
index = concatenated_tuple.index(element_to_search)
count = concatenated_tuple.count(element_to_search)

print("Concatenated tuple:", concatenated_tuple)
print("Index of element", element_to_search, ":", index)
print("Number of occurrences of element", element_to_search, ":", count)
