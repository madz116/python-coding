tax_rate=0.10
menu = {

"Burger": 150.00,

"Fries": 175.00,

"Soda": 30.00,

"Salad": 120.00,

"Pizza": 500.00,

"Ice Cream": 150.00,

"Coffee": 200.00,

"Tea": 50.00,

"Juice": 50.00,

"Pasta": 250.00,

"Sandwich": 125.00,

"Water": 10.00

}
order={}
def show_menu():
    print("\nMenu: ")
    for item, price in menu.items():
        print(f"{item}: ${price}")

def take_order():
    while True:
        item=input("\nEnter the item you want to order (type 'done' to finish.): ").strip()
        if item.lower()=='done':
            break
        if item in menu:
            quantity=int(input(f"Enter the quantity of {item}: "))
            if item in order:
                order[item]+=quantity
            else:
                order[item]=quantity
        else:
            print("Order not found in menu.")
def calculate_total():
    total=0.0
    for item, quantity in order.items():
        total+=menu[item]*quantity
    tax=total*tax_rate
    total_with_tax=tax+total
    return tax,total,total_with_tax

def print_bill():
    print("\n-----Bill Summary-----")
    total,tax,total_with_tax=calculate_total()
    for item, quantity in order.items():
        print(f"{item}x{quantity}=${menu[item]*quantity:.2f}")
    print(f"Subtotal: ${total:.2f}")
    print(f"Tax(10%): ${tax:.2f}")
    print(f"Total with tax: ${total_with_tax:.2f}")
    print("\n----------------------")

if __name__=="__main__":
    show_menu()
    take_order()
    print_bill()
    print("\nThank you for eating with us!")