temperatures = [1, 4, 8]


def forLoop(listTmp):
    for tmp in listTmp:
        print(tmp)


forLoop(temperatures)

for letter in "Virus":
    print(letter)


colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int):
        print(color)

grades = {"Bob": 9, "Jerry": 3, "Mike": 2}

for grade in grades.items():
    print(grade)

for grade in grades.keys():
    print(grade)

for grade in grades.values():
    print(grade)

phone_numbers = {"John Smith": "+37682929928",
                 "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{}: {}".format(key, value))


for phone in phone_numbers.values():
    print("00{}".format(phone[1:]))

username = ''
while username != "bob":
    username = input("Enter username: ")
print(f"thanks {username}")


while True:
    username = input("Enter username: ")
    if username == "pypy":
        break
    else:
        continue
