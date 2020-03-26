import time as t
import os
#import pandas

while True:
    if os.path.exists("../assets/resources/fruits.txt"):
        with open("../assets/resources/fruits.txt") as file:
            print(file.read())
    else:
        print("Files does not exist.")
    t.sleep(10)
