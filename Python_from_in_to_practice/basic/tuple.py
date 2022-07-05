dimensions = (200,50,)

print(dimensions)
print(dimensions[0])
print(dimensions[1])

print()
# dimensions[0] = 200   error unchangable
print("for")
for dimension in dimensions :
    print(dimension)

print()
print("change")
dimensions = (400,100,) # yes
print(dimensions)