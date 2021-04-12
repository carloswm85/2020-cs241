"""
File: .py
Author: Carlos W. Mercado
Class: CS241
Date: 05/18/2020

Description: Order class. It allows to work over a list of many
products. It provides the following information about the list:
Subtotal, Tax, Total. I can receive more products on the list,
display its content.
"""

class Order:
    def __init__(self):
        self.id = ""
        self.order_list = []
    
    def get_subtotal(self):
        self.subtotal = 0
        for item in self.order_list:
            self.subtotal += item.get_total_price()
        return self.subtotal
    
    def get_tax(self):
        self.tax = self.get_subtotal() * 0.065
        return self.tax
    
    def get_total(self):
        self.total = self.get_subtotal() + self.get_tax()
        return self.total
    
    def add_product(self, product):
        self.order_list.append(product)
    
    def display_receipt(self):
        print('Order: {}'.format(self.id))
        for item in self.order_list:
            item.display()
        print('Subtotal: ${:.2f}'.format(self.get_subtotal()))
        print('Tax: ${:.2f}'.format(self.get_tax()))
        print('Total: ${:.2f}'.format(self.get_total()))
            
            