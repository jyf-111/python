if False:
    print("true")
else:
    print("false")

a = 3
if a == 1:
    a += 1
    print("in 1")
elif a == 2 or a == 3:
    a += 1
    print("in 2")
else:
    print("end")

if a in (1, 2, 3):
    print("yes")
else:
    print("no")
