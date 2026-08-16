# Sorting of elements in the list(Ascending Order):

# Taking no. of elements in the list from the user:
MAX_LIST = int(input("Enter the total no. of elements in the list: "))

LIST = list()

# Taking the elements of the list from the user:
for i in range(MAX_LIST):
    num = int(input(f"Enter the {i+1} element of the list: "))
    LIST.append(num)

# Printing the unsorted elements of the list:
print(f"The Unsorted list of elements is: {LIST}")

# Now Sorting the list of elements in ascending order:
LIST.sort()  

# Finally, printing the sorted elements of the list:
print(f"The Sorted list of elements is: {LIST}")

