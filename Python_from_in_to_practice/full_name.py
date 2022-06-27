# python >= 3.6
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name}{last_name}"

print(full_name)
print(f"hello {full_name}")

# python < 3.6
print("{}{}".format(first_name,last_name))

# space
favorite_language = ' python '
print(favorite_language)
favorite_language = favorite_language.rstrip() # 暂时
print(favorite_language)