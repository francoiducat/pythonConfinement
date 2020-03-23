filePath = "../assets/resources/fruits.txt"
myfile = open(filePath)
print(myfile.read())
print(myfile.read())
myfile.close()


myfile = open(filePath)
print(myfile.read()[:15])
myfile.close()


def countCharInAFile(character, theFilePath):
    return open(filePath).read().count(character)


print(countCharInAFile("a", filePath))


with open(filePath, "r") as myFile:
    content = myFile.read()
print(content)
