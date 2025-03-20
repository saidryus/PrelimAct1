cities = tuple(input (f"Enter city {i+1}: ") for i in range (5))

ret = int(input("Enter index number to find a city: "))

if 0 <= ret < len (cities):
    print(f"Index {ret} contains: {cities[ret]}")
else:
    print("Invalid index! / City not found!")