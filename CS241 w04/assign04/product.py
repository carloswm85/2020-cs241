"""
File: .py
Author: Carlos W. Mercado
Class: CS241
Date: 05/18/2020

Description: Class of evert possible product. Required values are as listed.
"""

class Product:
    def __init__(self, id = '', name = '', price = 0.0, quantity = 0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total_price(self):
        return self.price * self.quantity
    
    def display(self):
        print('{} ({}) - ${:.2f}'.format(self.name, self.quantity, self.get_total_price()))
        
