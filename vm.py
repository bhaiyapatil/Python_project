class VendingMachine:
    products = {
        'coke': 25,
        'pepsi': 35,
        'soda': 45,
        'water': 20
    }
    coins = [5, 10, 20, 50, 100]

    def __init__(self):
       pass

    def select_product(self):
        print()
        print("* Welcome to the Vending Machine! *")
        print("\t   Products:")
        for product, price in self.products.items():
            print(f"\t{product} : {price} cents")

        product = input("\nenter the product which do you want to buy: ")
        if product in self.products:
            return product
        else:
            print("Invalid product selected.")
            return self.select_product()

    def insert_coins(self, total=0):
        coin = int(input("Please insert a coin (5, 10, 20, 50, 100): "))
        if coin in self.coins:
            total += coin
            print(f"Total amount inserted: {total} cents")
            if total >= self.products[self.selected_product]:
                return total
            else:
                return self.insert_coins(total)
        else:
            print("Invalid coin inserted.")
            return self.insert_coins(total)

    def calculate_change(self, total):
        change = total - self.products[self.selected_product]
        print(f"Change amount: {change} cents")
        return change

    def calculate_coins(self, change):
        coins_used = []
        while change > 0:
            for coin in reversed(self.coins):
                if coin <= change:
                    coins_used.append(coin)
                    change -= coin
                    break
        return coins_used

    def display_change(self, change, coins_used):
        if change == 0:
            print("you paid total amount")
        else:
            print("Coins to return:")
            for coin in coins_used:
                print(f"{coin} cents")
            print(f"\nCollect your total change: {change} cents")
        print(f"\nhere is your product {self.selected_product}\n\n\t Thank you!\n\tVIsit Again")

    def start(self):
        while True:
            self.selected_product = self.select_product()
            total = self.insert_coins()
            change = self.calculate_change(total)
            coins_used = self.calculate_coins(change)
            self.display_change(change, coins_used)
            con = input("\nEnter yes if you want to buy again: ")
            if con != 'yes':
                break


vm = VendingMachine()
vm.start()


 