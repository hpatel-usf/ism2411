# Self assesment
#1 I began debugging by looking at the traceback and finding where the program stopped. Print statements helped me follow variable values. This shows I know how to use error messages to locate problems, but I can get better at reviewing my code before asking for help.
#2 The apply_discount(price, tier) function uses a price and membership tier. It gives back the amount after applying a discount: gold receives 15% off, silver receives 10% off, bronze receives 5% off, and all other tiers receive nothing. Another person can use it by knowing the inputs and output.
#3 AI disclosure: I used ChatGPT to better understand Python mistakes and ideas like functions and variable scope. Its explanations helped me strengthen my knowledge and confirm how the code should work. I also used it to identify some mistakes in my code.


# EXERCISE 1

def calculate_tax(price, rate):
    return price * rate

print(calculate_tax(100, 0.07))
print(calculate_tax(250, 0.08))


# EXERCISE 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

price = 200

print(f"gold: ${apply_discount(price, 'gold'):.2f}")
print(f"silver: ${apply_discount(price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(price, 'bronze'):.2f}")
print(f"none: ${apply_discount(price, 'none'):.2f}")


# EXERCISE 3

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

price = 200
discounted = apply_discount(price, "gold")
total = final_price(price, "gold", 0.07)

print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${total:.2f}")
print(f'final_price(200, "gold", 0.07) = ${total:.2f}')


# EXERCISE 4

orders = [(200, "gold"), (150, "silver"),
          (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# EXERCISE 5

# broken_sales.py


# EXERCISE 6

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)
