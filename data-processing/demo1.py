import json

path = '../datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]



for var in records:
    print(var)

print(type(records))
print(dir(records))