import random
n = random.randint(0, 10)
w = int(input("ВВедите число от 0 до 10\n"))
print(n)
while n!= w:
    if w>n:
        print(f"Число которое вы ввели слишком большое и подсказка" , w-n)
        w = int(input("ВВедите число снова от 0 до 10\n"))
    elif w < n:
        print("Too low\n")
        w = int(input("ВВедите число снова от 0 до 10\n"))
    else:
        break
print("You win")