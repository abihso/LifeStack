lists = [1,2,3,4,5,6,7,8,9,10]

results = list(filter(lambda a : a % 2 == 2, lists))
print(results)

results2 = list(map(lambda a : a * 3,lists))

print(results2)