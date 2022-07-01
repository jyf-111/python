# 字典列表
alien_0 = {'color':'green','point':5}
alien_1 = {'color':'yellow','point':10}
alien_2 = {'color':'red','point':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens :
    print(alien)


# 字典中储存列表

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print(pizza['crust'])
print()

for topping in pizza['toppings']:
    print(topping)

# 字典中储存字典
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name:{full_name.title()}")
    print(f"\t{location.title()}")