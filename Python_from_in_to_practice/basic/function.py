def func():
    print("hello function")
func()

def func1(*a): # 任意数量实参
    print(a)
func1(1,2,3)

def func2(**a):
    print(a)
func2(a22="1111")