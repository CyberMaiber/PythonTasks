# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def Str_To_Bool (inp):
    if inp == "1":
        return True
    else:
        return False

for i in range(0, 8):
    text = "{0:03b}".format(i)
    x = Str_To_Bool(text[0])
    y = Str_To_Bool(text[1])
    z = Str_To_Bool(text[2])
    print(f"¬({x} ⋁ {y} ⋁ {z}) == ¬{x} ⋀ ¬{y} ⋀ ¬{z} =", end = " ")
    if not (x or y or z) == (not x and not y and not z):
        print("True")
    else:
        print("False")