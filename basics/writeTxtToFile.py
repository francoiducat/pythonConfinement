# with open("../assets/resources/vegetables.txt", "w") as myFile:
#     myFile.write("Tomatoes")
#     content = myFile.read()
# print(content)


with open("../assets/resources/vegetables.txt", "a+") as myFile:
    myFile.write("\nCucumber")
    myFile.seek(0)
    content = myFile.read()
print(content)
