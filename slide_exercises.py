float(5)
int(5.2)
print(max(5, 3))

print("python is powerful"[5])
print(str(123456)[-2])
print("hello"[::-1])
"HELLO".lower()

print(not("a" not in "a" and -5//4 == 0 or 2 == 2) and False)

age = 2020 - 1995
age *= 2
# Bad variable name
int_ = 1

x = [1.1, 1.2, 1.3, 1.4, "s", "a", True]
x.append(3)
x.append(5)
x.extend([2, 3])
x[0] = 24
temp = x[0]
x[0] = x[-1]
x[0] = temp
x.sort()
y = sorted(x)
print(x)

x = (1,2,3)
print(x[2])
index = x.index(2)
print(index)

x = {1,2,3}
y = {3,4,5}
print(x.intersection(y))
print(type({}))

dict_ = {
    "key1": "value1",
    "key2": "value2"
}
print(dict["key1"])
print(dict.get("key1"))
dict_["key3"] = "value3"

n = 5
if n == 0:
    print("tricky")
elif n % 2 == 0:
    print("yes")
else:
    print("no")

l = ["hello"]
if l:
    if "cheese" in l:
        print("found it")
    else:
        print("did not find it")
else:
    print("empty")

keys = []
for key in dict_:
    keys.append(key)
print(keys)

for i,c in enumerate("jeevan"):
    print(i, c)

for i in range(101):
    if i == 25:
        continue
    else:
        print(i)

l = [1,2,3,4,5,6,7,8]
n = 5
for i in l:
    print(i)
    if i == n:
        break

# while True:
#     print(1)

even = []
odd = []
for i in l:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

n = 5
result = 1
for i in range(n, 0, -1):
    result *= i


def small(x,y):
    # return min(x,y)
    if x < y:
        return x
    else:
        return y

def fn(x=None):
    if x:
        print(x)
    else:
        print("no")

l = [1,2,2,3,3,4]
def unique(l):
    result = []
    for i in l:
        if i not in result:
            result.append(i)
    return result

def area():
    length = input("length: ")
    breadth = input("breadth:  ")
    return length * breadth

def fn():
    result = []
    while True:
        x = input("enter a number: ")
        if x:
            result.append(x)
        else:
            break
    print(result)
    return


def create():
    f = open("delete.txt", "w")
    f.write("we goin ride till i can't no mo")
    f.close()


def append():
    f = open("delete.txt", "a")
    f.write("started from the bottom, now we here")
    f.close()

def read():
    f = open("delete.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)


def fn(l, n):
    assert type(l) == list and type(n) == int
    try:
        return l[n]
    except KeyError:
        return None

from random import randint
def fn(x,y):
    n = randint(x,y)
    return n

import datetime as dt
def current_date():
    return dt.datetime.now()


