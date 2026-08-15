ss =[
     { "Name": "Anna", "age": 23}, {"Name": "Jacobs", "age": 25},
     {"Name": "KK", "age" : 18 },
     {"Name": "Mario", "age": 24}
]

sorted_ss = sorted(ss, key= lambda j: j["age"])
namae = sorted(ss, key= lambda k: k["Name"])
criteria = lambda i: True if i["age"] <20 else False
under_20 = list(filter(criteria, ss))

print(sorted_ss)
print(namae)
print(under_20)
