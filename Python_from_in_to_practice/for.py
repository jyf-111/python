from ssl import OPENSSL_VERSION_INFO


magicians = ['alice','david','carolina']
for magician in magicians :
    print(magician)
    print('-')

print("-------------------------")
for value in range(1,5) :
    print(value)
print("-------------------------")
for value in range(6) :
    print(value)

print("-------------------------")
numbers = list(range(2,11,2))
print(numbers)

print("-------------------------")
squares = []
for value in range(1,10) :
    square = value ** 2
    squares.append(square)
print(squares)
print(f"min = {min(squares)}")
print(f"max = {max(squares)}")
print(f"sum = {sum(squares)}")

# 列表解析
squares = [value**2 for value in range(1,10)]
print(squares)

# 切片
print(squares[0:3])
print(squares[:5])
print(squares[-2:])

# 复制
copy = squares[:]
print(f"copy : {copy}")
