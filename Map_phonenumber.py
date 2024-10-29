n = int(input())
phonenumbers = {}
for i in range(0, n):
    entry = input().split()
    name = entry[0]
    number = entry[1]
    phonenumbers[name] = number

def retrieve_numbers(name):
    keys = phonenumbers.keys()
    if name in keys:
        print(name+'='+phonenumbers.get(name))
    else:
        print("Not found")
# Taking infifnite entries
while True:
    try:
        query = input()
        retrieve_numbers(query)
    except:
        break