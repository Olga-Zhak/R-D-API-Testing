from MyTestPython import mydata


def sum(all):
    for i in range(len(mydata)):
        total = len(mydata)
        print(mydata[total-1])

    print(f"Sum is equal {mydata[0]+mydata[1]+mydata[2]+mydata[3]+mydata[4]+mydata[5]+mydata[6]+mydata[7]+mydata[8]}")


def exceptfour(any):
    all_sum = 0
    for char in mydata:
        if char != 4:
            all_sum += char
        else:
            print('finish')
    print(all_sum)


