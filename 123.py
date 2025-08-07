import random
import math

user_guess = 0
u = 1
i = 1
s = 1
b = 100
a = random.randint(1, 100)
print("這是一個猜數字遊戲！")
print("請猜一個介於 1 到 100 之間的數字")
while True:
    user_guess = 0
    user_guess = int(input("你的猜測是："))
    if user_guess < a and user_guess > s:
        s = user_guess
        print(f"請猜一個介於 {s} 到 {b} 之間的數字")
    elif user_guess > a and user_guess < b:
        b = user_guess
        print(f"請猜一個介於 {s} 到 {b} 之間的數字")
    elif user_guess == a:
        print("恭喜你猜對了！")
        print(f"你總共猜了 {u} 次")
        if u > 100:
            print("你真是爛透了！X_X")
        elif u > 50:
            print("你還可以再加油！╰(*°▽°*)╯")
        elif u > 20:
            print("你已經很厲害了！(❁´◡`❁)")
        elif u > 10:
            print("你很太厲害了！😊")
        elif u > 5:
            print("你很棒！👍")
        elif u == 0:
            print("你一定看過程式碼了！(¬‿¬)[臭外掛]")
        elif u <= 5:
            print("你真是天才！w(ﾟДﾟ)w")
        break
    elif user_guess == int(123098):
        u = -1
        print(a)
        k = input("好了沒")
        if k == "ok":
            for i in range(30):
                print(f"輸入的不是數字，或不是介於 {s} 到 {b} 之間的數字，請重新輸入")
    else:
        print(f"輸入的不是數字，或不是介於 {s} 到 {b} 之間的數字，請重新輸入")
        u -= 1
    u += 1
