import json

# Save a list to a JSON file
my_list = [1, 2, 3, 4, 5]
with open('my_list.json', 'w') as file:
    json.dump(my_list, file)

# Load the list from the JSON file
with open('my_list.json', 'r') as file:
    loaded_list = json.load(file)

print(loaded_list)  # Output: [1, 2, 3, 4, 5]
