import json

numbers = [1,2,3,4,5,6]
filename = "Python_from_in_to_practice/numbers.json"
with open(filename,"w") as f:
    json.dump(numbers,f)

with open("Python_from_in_to_practice/numbers.json") as f:
    num = json.load(f)
    print(num)