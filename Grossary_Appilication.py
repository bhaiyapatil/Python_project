################## Grossary Billing Application    ########################
# Grossary={    
#     product_id :1  product_name:Maggie stock:200 price:23
#     product_id:2  product_name:Buscuits stock:1000 price:50
# }
# menu -
#      1. Add new Product
#      2. show all product
#      3. Update specific product
#      4. Delete product
#      5. purchase product

# 5. which product u want -- product_id  -- 2 
# how many qty u want - 20 
# price - 200
# pay - 200
# message -- Thanks for Visit our shop. Kindly collect your product
#     do u want to continue -- Y  then again display Menu otherwise
# exit from program

grocery_items = { 
     'product1': { 
          'product_name': 'maggie',  
          'stock': 1000,  
          'price': 10 
          }, 
     'product2': { 
          'product_name': 'chips',  
          'stock': 2000,  
          'price': 5 
          }, 
     'product3': { 
          'product_name': 'chocolate',  
          'stock': 1500,  
          'price': 5 
          }, 
     'product4': { 
          'product_name': 'milk',  
          'stock': 500,  
          'price': 50 
          }, 
     'product5': { 
          'product_name': 'sugar',  
          'stock': 100,  
          'price': 55 
          }, 
     'product6': { 
          'product_name': 'bread',  
          'stock': 100,  
          'price': 15 
          }, 
     'product7': { 
          'product_name': 'biscuit',  
          'stock': 2500,  
          'price': 10 
          }, 
     'product8': { 
          'product_name': 'salt',  
          'stock': 400,  
          'price': 25 
          }, 
     'product9': { 
          'product_name': 'chilli powder',  
          'stock': 300,  
          'price': 50 
          }, 
     'product10': { 
          'product_name': 'ice cream',  
          'stock': 100,  
          'price': 15 
          }, 
                 } 
 
while True: 
    print() 
    print("*****MENU*****") 
    print("1: Add new product") 
    print("2: Show all Product") 
    print("3: update specific product") 
    print("4: Delete Product") 
    print("5: purchase product") 
    choice = int(input("Enter your choice:  ")) 
    if choice == 1: 
        product_no,product_name,stock,price  = input("Enter the product no (like product11), product name, stock and price: ").split() 
        stock = int(stock) 
        price = int(price) 
        grocery_items[product_no] = {'product_name':product_name, 'stock':stock, 'price':price} 
        for key, value in grocery_items.items(): 
            print(f"{key}:{value}") 
     
    elif choice == 2: 
        for key, value in grocery_items.items(): 
            print(f"{key}:{value}") 
     
    elif choice == 3: 
        product_name = input("Enter the name of the product you want to update: ") 
        print(f"The product is {grocery_items[product_name]['product_name']}") 
        stock = int(input("Enter the new stock for the product: ")) 
        price = int(input("Enter the new price for product: ")) 
        grocery_items[product_name]['stock'] = stock 
        grocery_items[product_name]['price'] = price 
        for key, value in grocery_items.items(): 
            print(f"{key}:{value}") 
 
    elif choice == 4: 
        product_name = input("Enter the name of the product you want to delete: ") 
        print(f"{grocery_items[product_name]['product_name']} is deleted ") 
        del grocery_items[product_name] 
        for key, value in grocery_items.items(): 
            print(f"{key}:{value}") 
 
    elif choice == 5: 
        for i, j in grocery_items.items(): 
            print(f"{i}:{j}") 
        product_name = input("Enter the product no. like (product1) which you want to buy: ")     
        if product_name in grocery_items: 
            print(f"The product is {grocery_items[product_name]['product_name']}") 
            quantity = int(input("Entere the quantity of the product you want to buy: ")) 
            if quantity <= grocery_items[product_name]['stock']: 
                total = quantity * grocery_items[product_name]['price'] 
                grocery_items[product_name]['stock'] -= quantity 
                print(f"now the {grocery_items[product_name]['product_name']} stock available is {grocery_items[product_name]['stock']}") 
                print(f"Total cost of {quantity} {grocery_items[product_name]['product_name']} is {total}") 
                amount = int(input("Pay the total amount: ")) 
                if amount == total: 
                    print("Thank You! visit again") 
                elif amount > total: 
                    change = amount - total 
                    print(f"Here is your change {change}\nThank You! visit again")
            
            else: 
               print("You don't pay the total payment your order is cancel") 