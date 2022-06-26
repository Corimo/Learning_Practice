def accept(a, b):
    division = a / b
    def addition(a, b):
        return a + b

    add = addition(a, b)

    return add + 5

result = accept(10, 5)

print (result)