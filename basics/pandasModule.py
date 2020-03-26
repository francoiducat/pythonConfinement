import time
import os
import pandas

path = "../assets/resources/temperatures.csv"
while True:
    if os.path.exists(path):
        data = pandas.read_csv(path)
        print(data)
        print(data.mean())
        print(data.mean()["st1"])
    else:
        print("Files does not exist.")
    time.sleep(10)
