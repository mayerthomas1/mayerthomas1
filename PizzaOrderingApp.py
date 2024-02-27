class Pizza:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class OrderItem:
    def __init__(self, pizza, quantity):
        self.pizza = pizza
        self.quantity = quantity

    def get_total_price(self):
        return self.pizza.price * self.quantity


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.order_items = []

    def add_item(self, order_item):
        self.order_items.append(order_item)

    def remove_item(self, order_item):
        self.order_items.remove(order_item)

    def calculate_total_amount(self):
        total = 0
        for item in self.order_items:
            total += item.get_total_price()
        return total


class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone


class PizzaOrderApp:
    def __init__(self):
        self.orders = []

    def place_order(self, customer, order_items):
        order = Order(customer)
        for item in order_items:
            order.add_item(item)
        self.orders.append(order)
        return order





pizza1 = Pizza("Cheese", "Cheese pizza with tomato sauce", 18.99)
pizza2 = Pizza("Pepperoni", "Cheese, Pepperoni and Garlic Crust", 20.99)
pizza3 = Pizza("Supreme", "Cheese, Pepperoni, Mushroom, and Onion", 25.99)


item1 = OrderItem(pizza1, 3)
item2 = OrderItem(pizza3, 1)


customer = Customer("Homer Simpson", "123 Fake St.", "314-610-7888")


pizza_order_app = PizzaOrderApp()


order = pizza_order_app.place_order(customer, [item1, item2])


total_amount = order.calculate_total_amount()


print("New Order for:", order.customer.name)
print("Address for Delivery:", order.customer.address)
print("Ordered items:")
for item in order.order_items:
    print("  Pizza:", item.pizza.name)
    print("  Quantity:", item.quantity)
    print("  Price:", item.get_total_price())
print("Total Amount:", total_amount)
