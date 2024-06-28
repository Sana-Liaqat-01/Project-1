# step 2
inventory={}
total_sales=0

# step 3
def main ():
    print('Welcome to our inventory')
    
# step 4
def add_item (name, price, count):
    inventory[name]= {'price': price, 'count':count}
    print('item ', name + ' is added to inventory')
    
# step 5
def main():
    print('Welcome to our inventory')
    while True:
        print('1. add new item')
        choice=input('Enter your choice')
        if choice == '1':
            name=input('enter your item name')
            price=input('Enter price of item')
            count=input('Enter item count')
            add_item(name,price,count)

# step 6 Github


# step 7 
def buy_item(name, quantity):
    if name in inventory:
        if inventory[name]['count'] >= quantity:
            inventory[name]['count'] -= quantity
            total_price = inventory[name]['price'] * quantity
            global total_sales
            total_sales += total_price
            print(f"{quantity} {name}(s) bought successfully for ${total_price:.2f}.")
        else:
            print("Insufficient stock of '{}'.".format(name))
    else:
        print("Item '{}' not found in inventory.".format(name))
            
            
            
# step 8

def main():
    print('Welcome to our inventory')
    while True:
        print('1. add new item')
        print('2. Buy item')

        choice=input('Enter your choice')
        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            count = int(input("Enter item count: "))
            add_item(name, price, count)
        elif choice == '2':
            name = input('Enter item name :')
            new_price=float(input('Enter new price'))
            change_price(name, new_price)
   
# step 9
#github

# step 10

def change_price( name, new_price):
    if name in inventory:
        inventory[name]['price'] = new_price
        print('price of'+name + ' updated to $' + str(new_price))
    else:
        print(name + ' not found in inventory') 
        
# step 11

def main(name, new_price):
    print('Welcome to our inventory')
    while True:
        print('1. add new item')
        print('2. Buy item')
        print('3. Change price')
    
        choice=input('Enter your choice')
        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            count = int(input("Enter item count: "))
            add_item(name, price, count)
        elif choice == '2':
            name = input('Enter item name :')
            new_price=float(input('Enter new price'))
            change_price(name, new_price)
        elif choice == '3':
            name = input('Enter item name :')
            new_price=float(input('Enter new price'))
            change_price(name, new_price)
            
# step 12 
#github


# step 13
def display_inventory():
    print('current invenrory:')
    for item, details in inventory.items():
        print(f'{item}:${ details['price']}*{ details['count']}')
        print(f'total sales:${total_sales}')
    
    
    
# step 14


def main():
    print("Welcome to the Inventory Management System!")
    print("1. Add new item")
    print("2. Buy item")
    print("3. Change item price")
    print("4. Display inventory")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        count = int(input("Enter item count: "))
        add_item(name, price, count)
    elif choice == '2':
        name = input("Enter item name to buy: ")
        quantity = int(input("Enter quantity to buy: "))
        buy_item(name, quantity)
    elif choice == '3':
        name = input("Enter item name to change price: ")
        new_price = float(input("Enter new price: "))
        change_price(name, new_price)
    elif choice == '4':
        display_inventory()
        
    
# step 15
# GITHUB

#step 16

def update_inventory(name, new_count):
    if name in inventory:
        inventory[name]['count'] = new_count
        print("Inventory count of item '{}' updated to {}.".format(name, new_count))
    else:
        print("Item '{}' not found in inventory.".format(name))

# step 17

# inventory.py

def main():
    print("Welcome to the Inventory Management System!")
    while True:
        print("1. Add new item")
        print("2. Buy item")
        print("3. Change item price")
        print("4. Display inventory")
        print("5. Update inventory count")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            count = int(input("Enter item count: "))
            add_item(name, price, count)
        elif choice == '2':
            name = input("Enter item name to buy: ")
            quantity = int(input("Enter quantity to buy: "))
            buy_item(name, quantity)
        elif choice == '3':
            name = input("Enter item name to change price: ")
            new_price = float(input("Enter new price: "))
            change_price(name, new_price)
        elif choice == '4':
            display_inventory()
        elif choice == '5':
            name = input("Enter item name to update count: ")
            new_count = int(input("Enter new count: "))
            update_inventory(name, new_count)
            print(update_inventory)
print(inventory)
        
main()



     
            
            
            
            
            
            
            

