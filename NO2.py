price = list(float(input (f"Enter number {i+1}: ")) for i in range (5))

print("Original price list: ", price)
updated_price = float(input("Enter the updated price for the third item: "))
price[2]=updated_price
print(f"Updated price for the third item is: {price[2]}")
print("Updated price list: ", price)

