try:
    print(5/0)
except ZeroDivisionError:
    print('divide zero')
else:
    print("success")


try:
    with open("Python_from_in_to_practice/text.txt",encoding='utf-8') as filename:
        words = filename.read()
except FileNotFoundError:
    pass
else:
    print("success")
    word = words.split()
    print(word)
    print(len(word))
