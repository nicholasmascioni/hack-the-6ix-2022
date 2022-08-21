initial_list = []

with open('grocery_list.txt', 'r') as groceries:
    for grocery in groceries:
        initial_list.append(grocery.strip())

print(initial_list)
