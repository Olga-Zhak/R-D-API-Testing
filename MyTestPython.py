import json

mydata = [4, 4, 8, 3, 3, 3, 2, 4, 4]

for char in mydata:
    print(char)

for i in range(3):
    print(mydata[i])

def sum(all):
    for i in range(len(mydata)):
        total = len(mydata)
        print(mydata[total-1])
    print(f"All sum is equal {mydata[0]+mydata[1]+mydata[2]+mydata[3]+mydata[4]+mydata[5]+mydata[6]+mydata[7]+mydata[8]}")

sum(mydata)


def exceptfour(any):
    all_sum = 0
    for char in mydata:
        if char != 4:
            all_sum += char
    print(f'Sum except 4 is equal {all_sum}')

exceptfour(mydata)


with open('testjson.py', 'r') as lists_body:
    data = json.load(lists_body)
    print(data)
    print(data['lists'][0]['name'])
    print(data['lists'][0]['id'])
    for item in data['lists']:
        print(f"Name: {item['name']}, ID: {item['id']}")