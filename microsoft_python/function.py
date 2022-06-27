from datetime import datetime


def print_time(name):
    print(name)
    print(datetime.now())


print_time("start")
for i in range(0, 10):
    print()
print_time("end")
