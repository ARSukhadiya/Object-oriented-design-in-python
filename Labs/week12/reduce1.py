from functools import reduce

fruits = ["apple", "orange", "pears", "banana"]

# out = reduce(lambda x, y: x[0].capitalize()+x[1:] + ', ' + y[0].capitalize()+y[1:], fruits)
out = reduce(lambda x, y: (x + ', ' if x != "" else x) + y.capitalize(), fruits, "")

print(out)