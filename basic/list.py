jyf = {}
jyf["first"] = "蒋"
jyf["second"] = "雨峰"
# print(jyf)
# print(len(jyf))

gk = {"first": "葛", "second": "铠"}
# print(gk)
people = [jyf, gk]
print(people)

people.append({"first": "Bill", "second": "Gates"})
print(people)

presenters = people[0:2]
print(presenters)
