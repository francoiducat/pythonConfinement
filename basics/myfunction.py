import dictionary as dic


def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean


print(mean([1, 4, 5]))
print(mean(dic.mydict.values()))


def lengther(lst):
    return len(lst)


def area(square):
    return square*square
