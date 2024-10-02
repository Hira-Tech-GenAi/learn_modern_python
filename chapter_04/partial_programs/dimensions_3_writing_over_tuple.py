dimensions:tuple[int, str] = (200, "500")
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
#! error not allow
#dimensions:tuple[int,int] = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)