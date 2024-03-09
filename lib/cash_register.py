#!/usr/bin/env python3
# discount applied = 20%
#
class CashRegister:
    def __init__(self, discount=20==0):
        self.discount = discount
        self.items = []
        self.total = 0
        self.last_transaction_amount = 0
        
    def add_item(self, title, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        self.last_transaction_amount = item_cost  
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        elif self.discount > 0:
            discount_amount = self.total * (self.discount / 100.0)  
            self.total = int(self.total - discount_amount)  
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("Invalid discount value.")



    def void_last_transaction(self):
        if self.items:
            self.total -= self.last_transaction_amount
            self.items.pop()
            if not self.items:
                self.total = 0.0
        else:
            print("No items to void.")




        
            

       
        
  
