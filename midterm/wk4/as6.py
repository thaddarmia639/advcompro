grades = [22,35,54,45,68,72,93,39,56,90]
passedppl = list(filter(lambda i: i >= 60, grades))
passed_w_bonus = list(map(lambda j: j * 0.05, passedppl))

print(passed_w_bonus)
