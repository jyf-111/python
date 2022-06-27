from doctest import REPORTING_FLAGS


bicycles = ['trek','cannondale','redline','specialize']
print(bicycles)

print(bicycles[0])
print(bicycles[3])

print(bicycles[-1])

print(f"visit : {bicycles[-1].title()}")

print()

# 修改列表
bicycles[0] = 'car';
print(bicycles)
bicycles.append('aircraft')
print(f"after modify {bicycles}")



test = []
test.append(1)
test.append(2)
test.append(3)
test.append(4)
test.append(5)
print(f"after append {test}")

test.insert(0,"hihi")
print(f"insert {test}")

del test[0]
print(f"after delete {test}")


ret = test.pop()
print(f"after pop {test}")
print(f"ret = {ret}")

ret1 = test.pop(0)
print(f"after pop(0) {test}")
print(f"ret1 = {ret1}")


ret2 = test.remove(3)
print(f"after remove {test}")
print(f"ret2 = {ret2}") # remove无返回值

print()

# organize list
car = ['bmw','audi','toyota','subaru']
print(f" befor sort {car}")
print(f" sort {sorted(car)}") # 临时
print(f" after sort {car}") # 临时

car.sort(reverse=False)
print(f"after sort {car}") # 永久
car.sort(reverse=True) # or   car.reverse()
print(f"after sort {car}") # 永久
print(len(car))