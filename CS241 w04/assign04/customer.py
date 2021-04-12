"""
File: .py
Author: Carlos W. Mercado
Class: CS241
Date: 05/18/2020

Description: Customer class. Contains information about any costumer: Name and ID.
Every customer has a list of orders, every of which contain a list of products.
"""

class Customer:
    def __init__(self, id = '', name = '', orders = []):
        self.id = id
        self.name = name
        self.orders = orders        
    
    def get_order_count(self):
        return len(self.orders)
    
    # Returns the total amount of money spent in every product, from every order.
    def get_total(self):
        self.total_price = 0
        for order_totals in self.orders:
            self.total_price += order_totals.get_total()
        return self.total_price
    
    def add_order(self, order):
        self.orders.append(order)
    
    # Displays the overall total spent by the customer.
    def display_summary(self):
        print("Summary for customer '{}':".format(self.id))
        print('Name: {}'.format(self.name))
        print('Orders: {}'.format(self.get_order_count()))
        print('Total: ${:.2f}'.format(self.get_total()))
    
    # Displays the information about every receipt (order) owned by the costumer.
    def display_receipts(self):
        print("Detailed receipts for customer '{}':".format(self.id))
        print('Name: {}'.format(self.name))
        for order in self.orders:
            print()
            order.display_receipt()
        
        