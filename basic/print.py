if True:
    print("true", end=" ")
elif True:
    print("False", end=" ")
print("!!!!!!!!!!!!")

print("Hello World")

a = 1
b = "hel"
s = "hello,{},{}".format(a, b)
print(s)

s = "hello,{1},{0}".format(a, b)
print(s)

s = f"hello,{a},{b}"
print(s)
