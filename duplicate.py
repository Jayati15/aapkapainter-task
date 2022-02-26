def duplicate(a):
    arr = set()
    for i in range(len(a)):
        if a[i] in arr:
            return a[i]
        else:
            arr.add(a[i])

input_string = input()
list  = input_string.split()
res = duplicate(list)
print(res)