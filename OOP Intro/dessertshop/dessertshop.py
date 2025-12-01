from dessert import IceCream, Candy, Cookie, Sundae, Order
from tabulate import tabulate



class DessertShop:
    def user_prompt_candy(self):
        candy = input("What kind of candy?\n-->")
        candy_weight = round(float(input("Enter the weight(lbs)\n-->")),2)
        price_per_pound = round(float(input("Enter the price per pound\n-->")),2)
        return Candy(candy, candy_weight=candy_weight, price_per_pound=price_per_pound)
    
    def user_prompt_cookie(self):
        cookie = input("What kind of cookies?\n-->")
        cookie_ammount = int(input("Enter the ammount\n-->"))
        price_per_dozen = round(float(input("Enter the price per dozen\n-->")),2)
        return Cookie(cookie, cookie_ammount=cookie_ammount, price_per_dozen=price_per_dozen)
    
    def user_prompt_icecream(self):
        ice_cream = input("What kind of ice cream?\n-->")
        scoop_count = int(input("Enter the number of scoops\n-->"))
        price_per_scoop = round(float(input("Enter the price per scoop\n-->")),2)
        return IceCream(ice_cream, scoop_count=scoop_count, price_per_scoop=price_per_scoop)
    
    def user_prompt_sundae(self):
        sundae = input("What kind of ice cream?\n-->")
        topping = input("What topping?\n-->")
        scoop_count = int(input("Enter the number of scoops\n-->"))
        topping_price = round(float(input("Enter the topping price\n-->")))
        price_per_scoop = round(float(input("Enter the price per scoop\n-->")))
        return Sundae(sundae, topping_name=topping, scoop_count=scoop_count, topping_price=topping_price, price_per_scoop=price_per_scoop)






def collect_payment(order):
    payment = input("\nHow will you pay?(1-3)\n-->")
    if payment == "1":
       order.set_pay_type("CASH")
    elif payment == "2":
       order.set_pay_type("CARD")
    elif payment == "3":
       order.set_pay_type("PHONE")
    else:
       print("Payment Type is invalid") 
       collect_payment(order)

def main():
    order = Order()
    shop = DessertShop()

    prompt = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',            
            '3: Ice Cream',
            '4: Sundae',
            '\nWhat would you like to add to the order? (1-4, Enter for done)\n-->'
      ])


    done = False
    while not done:
      choice = input(prompt)
      match choice:
        case '':
          done = True
        case '1':            
          item = shop.user_prompt_candy()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '2':            
          item = shop.user_prompt_cookie()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '3':            
          item = shop.user_prompt_icecream()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '4':            
          item = shop.user_prompt_sundae()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case _:            
          print('Invalid response:  Please enter a choice from the menu (1-4) or Enter\n-->')
    print("\n\n\n")
    print("""1:CASH
2:CARD
3:PHONE""")
    

    collect_payment(order)
    order.sort()
      


    print("\n\n\n\n")
    print(tabulate(order.to_list(), headers = ["Name", "Cost", "Tax"], tablefmt="fancy_grid"))
    print("-----------------------------------")
    print(f"Paid with {order.get_pay_type()}")
    print("-----------------------------------")
    print("\n\n")
    

    

    

if __name__ == "__main__":
    main()

