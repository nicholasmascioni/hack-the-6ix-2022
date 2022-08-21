from database import freshco_database, no_frills_database, t_and_t_database, walmart_database
initial_list = []
total = [0, 0, 0, 0]
min_dict = {}

with open('grocery_list.txt', 'r') as groceries:
    for grocery in groceries:
        initial_list.append(grocery.strip())

for grocery in initial_list:
    amount = int(grocery[0])
    item = grocery[1:].strip()
    min_dict[item] = []
    

    if item in freshco_database:
        min_dict[item].append(freshco_database[item])  
        total[0] = total[0] + (amount * freshco_database[item])
    if item in no_frills_database:
        min_dict[item].append(no_frills_database[item]) 
        total[1] = total[1] + (amount * no_frills_database[item])
    if item in t_and_t_database:
        min_dict[item].append(t_and_t_database[item]) 
        total[2] = total[2] + (amount * t_and_t_database[item])
    if item in walmart_database:
        min_dict[item].append(walmart_database[item]) 
        total[3] = total[3] + (amount * walmart_database[item])

    if item in freshco_database:
        if freshco_database["price_match"]:
            total[0] = total[0] + (amount * int(min(min_dict[item])))
        else:
            total[0] = total[0] + (amount * freshco_database[item])
    if item in no_frills_database: 
        if no_frills_database["price_match"]:
            total[1] = total[1] + (amount * int(min(min_dict[item])))
        else:
            total[1] = total[1] + (amount * no_frills_database[item])
    if item in t_and_t_database:
        if t_and_t_database["price_match"]:
            total[2] = total[2] + (amount * int(min(min_dict[item])))
        else:
            total[2] = total[2] + (amount * t_and_t_database[item])
    if item in walmart_database: 
        if walmart_database["price_match"]:
            total[3] = total[3] + (amount * int(min(min_dict[item])))
        else:        
            total[3] = total[3] + (amount * walmart_database[item])


total = [int(x) for x in total]
print(total)



   
