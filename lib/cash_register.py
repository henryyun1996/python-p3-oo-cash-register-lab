#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.last_item = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    for num in range(quantity):
      self.items.append(title)
    self.last_item = [price, quantity]
  
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = int(self.total) * (100 - self.discount) / 100
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def get_items(self):
    return self.items
  
  def void_last_transaction(self):
    num = self.last_item[1]
    self.items = self.items[:num]
    self.total -= self.last_item[0] * self.last_item[1]