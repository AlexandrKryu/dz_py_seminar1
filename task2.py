# """ Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """


def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    newxyz = []
    for i in range(x):
        newxyz.append(input(f"Введите значение {xyz[i]}: "))
    return newxyz


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

xyz = inputNumbers(3)

if checkPredicate(xyz) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")