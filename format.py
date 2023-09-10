# We cannot combine strings and number simply 
# We use format() method for this 

age = 19
text = "My age is {}"
print (text.format(age))

# Using of indexes to make sure arguments are placed in right order

quantity = 3
item_no = 22
price = 120

order = "I want to place an order for item no {1} of quantity {0} at price {2}"

print(order.format(quantity , item_no , price))