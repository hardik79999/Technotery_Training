"""
Create a cart counter:

Takes customer name
Takes number of items
Stores item names in list
Stores prices in list
Calculates total
Applies discount if total > 500
Stores bill in tuple

"""
main_dict = {}
status = True

while status:
    customer_list = []
    d = {}

    print("----------welcome----------")
    menu = {
        "pizza": 200,
        "burger": 150,
        "vadapav": 50,
        "dabeli": 30
    }

    print(menu)
    Total = 0

    c_name = input("Enter Your Name : ")

    c_status = True
    while c_status:
        c_items = input("Enter Your choice : ").lower()

        if c_items in menu:
            no_items = int(input(f"How many {c_items} You want ??? : "))
            Total += no_items * menu[c_items]
            customer_list.append((c_items, no_items))
        else:
            print("Invalid input....!!!!")

        c_choice = input("Do you want add more items ??? (yes/no): ").lower()
        if c_choice == 'no' or c_choice == 'n':
            c_status = False

    # Discount calculation
    if Total > 500:
        discount = Total * 20 / 100
        Net_amount = Total - discount

        d["Customer Name"] = c_name
        d["Customer Items"] = customer_list
        d["Total"] = Total
        d["Applies discount"] = "20%"
        d["Total discount"] = discount
        d["Net Amount"] = Net_amount

        main_dict[c_name] = d

    else:
        Net_amount = Total

        d["Customer Name"] = c_name
        d["Customer Items"] = customer_list
        d["Total"] = Total
        d["Net Amount"] = Net_amount

        main_dict[c_name] = d

    choice = input("Do you want Add++ more customers (yes/no) : ").lower()
    if choice == 'no' or choice == 'n':
        status = False
        print("\n----------------Total Bill :::-------------------")
        for k, v in main_dict.items():
            print(k, ":", v)
        print("---------------------------------------------------")
