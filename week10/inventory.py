# Reflection 1:
# I was surprised that Python lists start counting at zero and allow negative indices to access items from the end. I also did not expect slicing to make it so easy to select several items without writing a loop.

# Reflection 2: 
# At Bubbakoos Burritos, a Python list could help track ingredient quantities and identify which ingredients need restocking. This could save time compared to manually checking and filtering rows in Excel during each shift.


# Exercise 1: Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


# Exercise 2: Index practice
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# Exercise 3: Slicing
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4: Modify
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5: Tuple comparison
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed, which helps protect fixed coordinates.")

print(coords)


# Exercise 6: Average of a list of sales
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7: Accumulator pattern
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original:", prices)
print("Discounted:", discounted)


# Exercise 8: Filter above threshold
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))