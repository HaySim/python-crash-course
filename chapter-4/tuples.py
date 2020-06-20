# tuples are technically defined by the presence of a comma; the parentheses make them look more readable.

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# writing over a tuple:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
