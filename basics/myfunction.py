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


def isIntInstance(x):
    return isinstance(x, int)


print('isIntInstance(3) is', isIntInstance(3))
print('isIntInstance("3") is', isIntInstance('3'))

# Ternary Operator


def warmOrCold(temp):
    return "Warm" if temp > 7 else "Cold"


def HotWarmOrCold(temp):
    if temp > 25:
        return 'Hot'
    elif 14 < temp < 26:
        return 'Warm'
    else:
        return 'Cold'


def process(*args):
    return sorted([value.upper() for value in args])


def keyWordArgs(**kwargs):
    return kwargs


print(keyWordArgs(a=1, b=2, c=3))


def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a=1, b=8))
