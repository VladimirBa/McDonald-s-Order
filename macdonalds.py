print("Welcome to McDonald's. Please select from the menu:")
print('''Today's menu is: 
"A. Cheeseburger - $0.99" 
"B. McChicken - $1.99"
"C. Big Mac - $3.99"
"A. Coke - $0.49"
"B. Diet Coke - $0.49"
"C. Sprite - $0.49"
"A. Caesar - $2.49"
"B. Grilled Chicken - $3.49"
"C. Green salad - $2.99"''')

total = 0
bur_order = ''
bur_num = ''
bur_sel = input('''Would you like a burger? Please type 'Y' for "Yes" or 'N' for "No": ''').upper()
if bur_sel == "Y":
    bur_sel_item = input("Please choose A, B or C ").upper()
    bur_num = int(input("How many would you like? "))
    if bur_sel_item == "A":
        bur_order += "Cheeseburger"
        total += bur_num * 0.99
    elif bur_sel_item == "B":
        bur_order += "McChicken"
        total += bur_num * 1.99
    else:
        bur_order += "Big Mac"
        total += bur_num * 3.99

sal_order = ''
sal_num = ''
sal_sel = input('''Would you like to add a salad? Please type 'Y' for "Yes" or 'N' for "No": ''').upper()
if sal_sel == "Y":
    sal_sel_item = input("Please choose A, B or C ").upper()
    sal_num = int(input("How many would you like? "))
    if sal_sel_item == "A":
        sal_order += "Caesar"
        total += sal_num * 2.49
    elif sal_sel_item == "B":
        sal_order += "Grilled Chicken"
        total += sal_num * 3.49
    else:
        sal_order += "Green salad"
        total += sal_num * 2.99

drink_order = ''
drink_num = ''
drink_sel = input('''Would you like to add a drink? Please type 'Y' for "Yes" or 'N' for "No": ''').upper()
if drink_sel == "Y":
    drink_sel_item = input("Please choose A, B or C ").upper()
    drink_num = int(input("How many would you like? "))
    if drink_sel_item == "A":
        drink_order += "Coke"
        total += drink_num * 0.49
    elif drink_sel_item == "B":
        drink_order += "Diet Coke"
        total += drink_num * 0.49
    else:
        drink_order += "Sprite"
        total += drink_num * 0.49

print(" *" * 20)
print("Here is your order details:")
print(f"The items you ordered are:", bur_num, bur_order, sal_num, sal_order, drink_num, drink_order)
print(f"Your total: ${total:.2f}")
