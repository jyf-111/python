try:
    a = 1/0
except ZeroDivisionError as e:
    print("fuck"+str(e))
else:
    print("else")
finally:
    print("final")
