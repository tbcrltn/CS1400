from abc import ABC, abstractmethod
from payment import PayType, Payable

class DessertItem(ABC):
    def __init__(self, name, tax_percent = 7.25):
        self.name = name
        self.tax_percent = tax_percent
    
    @abstractmethod
    def calculate_cost(self):
        pass
    
    def calculate_tax(self):
        price = self.calculate_cost() * (self.tax_percent/100)
        return round(price, 2)
    
    def __eq__(self, other):
        return self.calculate_cost() == other.calculate_cost()
    
    def __gt__(self, other):
        return self.calculate_cost() > other.calculate_cost()
    
    def __lt__(self, other):
        return self.calculate_cost() < other.calculate_cost()
    
    def __ge__(self, other):
        return self.calculate_cost() >= other.calculate_cost()
    
    def __le__(self, other):
        return self.calculate_cost() <= other.calculate_cost()
    


class Candy(DessertItem):
    def __init__(self, name, candy_weight = 0.0, price_per_pound = 0.0, packaging = "Bag"):
        DessertItem.__init__(self, name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = packaging

    def calculate_cost(self):
        return round(self.candy_weight * self.price_per_pound, 2)
    
    def __str__(self):
        
        return f"{self.name} - ({self.packaging})\n-     {self.candy_weight} lbs. @ ${self.price_per_pound}/lb,${self.calculate_cost()},[Tax: ${self.calculate_tax()}]"

    
class Cookie(DessertItem):
    def __init__(self, name, cookie_ammount, price_per_dozen, packaging = "Box"):
        DessertItem.__init__(self, name)
        self.cookie_ammount = cookie_ammount
        self.price_per_dozen = price_per_dozen
        self.packaging = packaging
    
    def calculate_cost(self):
        return round(self.cookie_ammount * (self.price_per_dozen/12),2)

    def __str__(self):
        return f"{self.name} - ({self.packaging})\n-     {self.cookie_ammount} cookies. @ ${self.price_per_dozen}/dozen,${self.calculate_cost()},[Tax: ${self.calculate_tax()}]"




class IceCream(DessertItem):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0, packaging = "Bowl"):
        DessertItem.__init__(self, name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = packaging
    
    def calculate_cost(self):
        return round(self.scoop_count * self.price_per_scoop, 2)
    
    def __str__(self):
        return f"{self.name} - ({self.packaging})\n-     {self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop,${self.calculate_cost()},[Tax: ${self.calculate_tax()}]"

    


class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name = "", topping_price = 0, packaging = "Boat"):
        IceCream.__init__(self, name, scoop_count=scoop_count, price_per_scoop=price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = packaging

    def calculate_cost(self):
        return round((self.scoop_count * self.price_per_scoop)+ self.topping_price, 2)


    def __str__(self):
        return f"{self.name} - ({self.packaging})\n-     {self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop\n-     {self.topping_name} topping @ ${self.topping_price},${self.calculate_cost()},[Tax: ${self.calculate_tax()}]"
    


class Order:
    def __init__(self):
        self.order = []
        self._pay_type = None

    def __str__(self):
        result = ";".join(str(item) for item in self.order)
        return result

    def __len__(self):
        return len(self.order)  
    
    def to_list(self):
        data = []
        big_list = str(self).split(";")
        for item in big_list:
            small_list = item.split(",")
            data.append(small_list)
        
        #data.append(["----------------------------", "------", "-----------"])
        data.append(["Order Subtotal: ", self.order_tax(), self.order_cost()])
        data.append(["Order Total: ", "-----", round(self.order_tax()+self.order_cost(),2)])
        data.append(["Items in Order: ", "-----", len(self.order)])
        return data


 
    def add(self, item):
        self.order.append(item)

    def print_names(self):
        for item in self.order:
            print(item.name) 

    def order_cost(self):
        total_cost = 0
        for item in self.order:
            total_cost += item.calculate_cost()
        return round(total_cost,2)

    def order_tax(self):
        total_tax = 0
        for item in self.order:
            total_tax += item.calculate_tax()
        return round(total_tax, 2)
    
    def get_pay_type(self) -> PayType:
        if self._pay_type not in ("CASH", "CARD", "PHONE"):
            raise ValueError(f"Invalid Pay Type: {self._pay_type}")
        return self._pay_type
    
    def set_pay_type(self, payment_method: PayType) -> None:
        if payment_method not in ("CASH", "CARD", "PHONE"):
            raise ValueError(f"Cannot store -> Invalid Pay Type: {payment_method}")
        self._pay_type = payment_method

    def sort(self):
        new_list = sorted(self.order)
        self.order = new_list
    

            



