num = list (map(int,input("Enter a list of numbers: ").split()))
conversion_num = tuple(num)
num_count = int (input("Enter a number to count: "))
counting = num.count(num_count)

print (f"The number {num_count} appears {counting} times")