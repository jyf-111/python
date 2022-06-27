def get_init(name, force_uppercase=False):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input("your first name")
print(get_init(force_uppercase=True, name="jyf"))
