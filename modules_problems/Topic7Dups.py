
input_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
seen = set()
result = []
for item in input_list:
    if item not in seen:
        result.append(item)  # Add item to result if not already in seen
        seen.add(item)  # Add item to the set to track duplicates
print(result)
