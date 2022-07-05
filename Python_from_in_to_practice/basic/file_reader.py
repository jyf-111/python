from multiprocessing import context

# read
with open('Python_from_in_to_practice/text.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())


print()
file = open('Python_from_in_to_practice/text.txt')
for line in file:
    print(line.rstrip())


print()
with open('Python_from_in_to_practice/text.txt') as file:
    lines = file.readlines()
for line in lines:
    print(line.rstrip())
    

# write
filename = 'Python_from_in_to_practice/text.txt'
with open(filename,'w') as file_object:
    file_object.write('i lov programing')