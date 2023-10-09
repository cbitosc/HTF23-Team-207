import math

class GroceryItem:
    def init(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def str(self):
        return f"{self.name} - Price: ${self.price:.2f}, Time: {self.time} minutes"

class GroceryStore:
    def init(self, name, location):
        self.name = name
        self.location = location

    def calculate_distance(self, customer_location):
        x1, y1 = customer_location
        x2, y2 = self.location
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        return distance

class GroceryApp:
    def init(self, customer_location):
        self.item_list = [
            GroceryItem("Apples", 2.5, 2),
            GroceryItem("Milk", 1.0, 1),
            GroceryItem("Bread", 1.5, 1),
            GroceryItem("Eggs", 2.0, 2),
            GroceryItem("Chicken", 5.0, 10),
            GroceryItem("Rice", 3.0, 5),
            GroceryItem("Cereal", 4.0, 3),
        ]
        self.store_list = [
            GroceryStore("Store USHODAYA", (1, 2)),
            GroceryStore("Store  SPENCERS", (3, 4)),
            GroceryStore("Store RELIANCE", (5, 6)),
        ]
        self.shopping_cart = []

        self.customer_location = customer_location

    def add_item_to_cart(self, item):
        self.shopping_cart.append(item)

    def optimize_shopping(self, budget, time_limit):
        self.shopping_cart = []
        sorted_items = sorted(self.item_list, key=lambda x: (x.price, -x.time))
        total_cost = 0.0
        total_time = 0

        for item in sorted_items:
            if total_cost + item.price <= budget and total_time + item.time <= time_limit:
                self.add_item_to_cart(item)
                total_cost += item.price
                total_time += item.time

    def find_nearest_store(self):
        nearest_store = min(self.store_list, key=lambda store: store.calculate_distance(self.customer_location))
        return nearest_store

    def view_shopping_cart(self):
        print("Shopping Cart:")
        for item in self.shopping_cart:
            print(item)

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.shopping_cart)
        return total_price

if name == "main":
    customer_location = (0, 0)  # Replace with the customer's actual location
    app = GroceryApp(customer_location)

    budget = float(input("Enter your budget: $"))
    time_limit = int(input("Enter your time limit (minutes): "))

    app.optimize_shopping(budget, time_limit)
    nearest_store = app.find_nearest_store()

    app.view_shopping_cart()
    total_price = app.calculate_total_price()

    print(f"\nNearest Store: {nearest_store.name}")
    print(f"Total Price: ${total_price:.2f}")