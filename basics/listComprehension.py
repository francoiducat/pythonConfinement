temps = [221, 543, 765, 766]

new_temps = [temp / 10 for temp in temps]

print(new_temps)

liste = [1, "abc", 2, "def"]


def onlyNumbers(alist):
    print([value for value in alist if isinstance(value, int)])


onlyNumbers(liste)

numberListe = [5, -5, 2, -1]


def onlyPositiveNumbers(alist):
    print([value if value > 0 else 0 for value in alist])


onlyPositiveNumbers(numberListe)


def doTheSum(lst):
    print(sum([float(i) for i in lst]))


doTheSum(numberListe)
