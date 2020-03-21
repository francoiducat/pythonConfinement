def warmOrCold(temp):
    return 'Warm' if temp > 7 else 'Cold'


userInput = int(input("Enter Temperature:"))

print(warmOrCold(userInput))
