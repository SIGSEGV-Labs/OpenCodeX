item = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = input("Enter quantity: ")

subtotal = price * quantity
discount = subtotal * 10 / 100
final_price = subtotal - discount

print("Item:", item)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Price:", final_price)

if final_price > 1000:
    print("You get free delivery!")
