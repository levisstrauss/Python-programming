# Linear search in python
def linearSearch(A, key):
    position = 0
    flag = False
    while position < len(A) and not flag:
        if A[position] == key:
            flag = True
        else:
            position += 1
    return flag


A = [84, 21, 47, 96, 15]
found = linearSearch(A, 150)
print(found)
