import random

i = 1
s = 1
b = 100
a = random.randint(1, 100)
print("這是一個猜數字遊戲！")
print("請猜一個介於 1 到 100 之間的數字")
while True:
    user_guess = 1
    user_guess = int(input("你的猜測是："))
    if user_guess < a:
        s = user_guess
        print(f"請猜一個介於{s} 到 {b} 之間的數字")
    elif user_guess > a:
        b = user_guess
        print(f"請猜一個介於 {s} 到 {b} 之間的數字")
    elif user_guess == a:
        print("恭喜你猜對了！")
        break
