alien_0 = {'color':'green','point':5}

print(alien_0['color'])
print(alien_0['point'])

# add

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# delete
del alien_0['x_position']
del alien_0['y_position']

print(alien_0)

# get 有检测
print(alien_0.get('speed'),"no such value")

print();
print();

for k,v in alien_0.items() :
    print(f"{k}:{v}")

for k in alien_0.keys() :
    print(k)

for v in set(alien_0.values()) : # set 去重 sorted 排序
    print(v)