import streamlit as st

with st.expander("Class1筆記"):
    st.write(
        """
    這裡是你今天學到的 Python 內容，用國小六年級能懂的方式幫你整理：

---

## 一、註解

註解是寫給人看的，電腦不會執行。

* 單行註解：

```python
# 這是單行註解
```

* 多行註解：

```python
\"""
這是多行註解
\"""
```

* 快速註解／取消註解：

```
按 Ctrl + ? 鍵
```

---

## 二、顯示文字（print）

讓電腦在畫面（終端機）上顯示文字或數字：

```python
print("Hello World!")  # 顯示文字
print(123)             # 顯示數字
```

---

## 三、基本型態

資料有不同種類：

| 種類（型態）      | 說明          | 例子               |
| ----------- | ----------- | ---------------- |
| 整數 (int)    | 沒有小數點的數字    | `1, -1, 0, 10`   |
| 浮點數 (float) | 有小數點的數字     | `1.0, 3.14`      |
| 字串 (str)    | 文字，必須用引號包起來 | `"apple", "123"` |
| 布林值 (bool)  | 表示對或錯       | `True, False`    |

---

## 四、變數

用來儲存資料的小盒子，可以取名字：

```python
a = 10      # 把整數10放進a裡
print(a)    # 顯示a裡的東西（會顯示10）

a = "apple" # 把文字"apple"放進a裡
print(a)    # 顯示a裡的東西（會顯示apple）
```

---

## 五、運算符號（運算子）

讓電腦做數學運算：

| 運算符號 | 意思            | 範例               |
| ---- | ------------- | ---------------- |
| `+`  | 加法            | `1 + 1` → `2`    |
| `-`  | 減法            | `5 - 2` → `3`    |
| `*`  | 乘法            | `3 * 2` → `6`    |
| `/`  | 除法            | `10 / 2` → `5.0` |
| `//` | 取商（除法後只取整數部分） | `7 // 2` → `3`   |
| `%`  | 取餘數           | `7 % 2` → `1`    |
| `**` | 次方            | `2 ** 3` → `8`   |

---

## 六、計算順序

數學運算的順序：

1. 括號 `( )`
2. 次方 `**`
3. 乘、除、取商、取餘數 `* / // %`
4. 加、減 `+ -`

例子：

```python
print((2 + 3) * 4)  # 會先算括號裡 2+3=5，再乘4 → 結果是20
```

---

## 七、字串運算

字串可以用加號 `+` 和乘號 `*`：

```python
print("apple" + " pen") # 連起來 → "apple pen"
print("apple" * 3)      # 重複3次 → "appleappleapple"
```

---

## 八、函式（內建功能）

Python 內建的一些功能叫做函式：

* **len()**：計算字串長度。

```python
print(len("apple"))  # 顯示5，因為"apple"有5個字母
```

* **type()**：看變數的型態。

```python
print(type(1))        # 顯示整數型態 int
print(type("apple"))  # 顯示字串型態 str
```

---

## 九、型態轉換

把一種型態的資料轉成另一種：

| 轉換函式      | 說明    | 範例                                |
| --------- | ----- | --------------------------------- |
| `int()`   | 轉成整數  | `int(1.5)` → `1`                  |
| `float()` | 轉成浮點數 | `float("1.23")` → `1.23`          |
| `str()`   | 轉成字串  | `str(123)` → `"123"`              |
| `bool()`  | 轉成布林值 | `bool(0)` → `False`，其他數字 → `True` |

* 錯誤例子：

```python
int("hello") # 錯誤！因為 "hello" 無法變成整數
```

---

## 十、讓使用者輸入（input）

讓使用者自己輸入資料：

```python
a = input("請輸入文字：")  # 電腦會等你輸入後，存到a裡
print(a)  # 顯示你輸入的文字
```

用 **input()** 輸入的內容都是字串，如果要當數字用，必須先轉換：

```python
數字 = int(input("輸入一個數字："))
print(數字 + 10)  # 如果你輸入10，會顯示20
```

---

## 十一、計算練習

計算圓面積：

```python
半徑 = int(input("輸入圓的半徑："))
面積 = 半徑 * 半徑 * 3.14
print(面積)
```

計算平均成績：

```python
期中 = int(input("輸入期中成績："))
期末 = int(input("輸入期末成績："))
平均 = (期中 + 期末) / 2
print("平均成績是：", 平均)
```

---

這樣就把今天上課學到的 Python 全部整理好了，記得多練習喔！

    """
    )
with st.expander("Class2筆記"):
    st.write(
        """
這裡用國小六年級能懂的方式，幫你簡單整理今天學到的 Python 內容：

---

## 一、輸入與數字運算

你可以請使用者輸入成績，然後計算平均：

```python
chA = int(input("輸入第一次國文成績："))
chB = int(input("輸入第二次國文成績："))

chAB = (chA + chB) / 2
print(chAB)  # 顯示平均分數
```

> **重點**：
>
> * `input()` 讓使用者輸入資料
> * `int()` 可以把字串變成數字，這樣才能計算
> * `(a+b)/2` 算出兩次成績的平均分數

---

## 二、字串格式化（f-string）

把變數放進字串裡顯示出來：

```python
name = "小明"
age = 18

print(f"hello,my name is {name}, I am {age} years old")
# 會顯示：hello,my name is 小明, I am 18 years old
```

> **重點**：
>
> * 字串裡用 `{}` 就能放入變數，這樣顯示起來就更方便

---

## 三、比較運算子（比大小、相等）

用來比較數字或資料的大小、相等或不同：

| 符號   | 意義    | 範例       | 結果      |
| ---- | ----- | -------- | ------- |
| `==` | 等於    | `1 == 1` | `True`  |
| `!=` | 不等於   | `1 != 1` | `False` |
| `>`  | 大於    | `2 > 1`  | `True`  |
| `<`  | 小於    | `1 < 2`  | `True`  |
| `>=` | 大於或等於 | `1 >= 1` | `True`  |
| `<=` | 小於或等於 | `1 <= 1` | `True`  |

---

## 四、邏輯運算子（and、or、not）

用來判斷兩個或多個條件：

* **and（而且）**：兩個條件都要成立才是 True

```python
print(True and True)   # True
print(True and False)  # False
```

* **or（或）**：只要一個條件成立就是 True

```python
print(True or False)   # True
print(False or False)  # False
```

* **not（不是）**：把結果變相反

```python
print(not True)        # False
print(not False)       # True
```

---

## 五、計算與判斷順序

Python 中有計算的優先順序（從最先算的到最後算的）：

1. `( )` 括號裡的東西最先算
2. `**` 次方
3. `* / // %` 乘、除、取商、取餘數
4. `+ -` 加、減
5. `== != > < >= <=` 比較大小
6. `not`
7. `and`
8. `or`

---

## 六、if 條件判斷（像門一樣）

你可以讓電腦依照使用者輸入的密碼來決定要做什麼：

```python
password = input("請輸入密碼：")

if password == "1234":
    print("歡迎 Jeffrey")
elif password == "5678":
    print("歡迎 Tim")
elif password == "0000":
    print("歡迎 Chloe")
else:
    print("密碼錯誤")
```

* `if` 是「如果」，成立就會做裡面的動作。
* `elif` 是「否則如果」，前面的條件不成立，才會檢查這個條件。
* `else` 是「否則」，全部條件都不成立時才會執行。

> **重點**：
>
> * 用 `elif` 可以省下時間，因為只要有一個成立後面就不再檢查。
> * 如果用很多個 `if`，電腦每一個都會檢查，會比較慢。

---

以上就是你今天學到的 Python 內容囉！記得多練習～😊

        """
    )
with st.expander("Class3筆記"):
    st.write(
        """
這裡用國小六年級可以懂的方式，幫你整理今天學到的 Python 知識：

---

# 一、Streamlit（網頁工具）

Streamlit 可以做簡單的網頁，像是輸入數字或顯示按鈕。

### ① 輸入數字

讓使用者輸入數字：

```python
import streamlit as st

number = st.number_input("請輸入數字", step=1, min_value=0, max_value=100)
st.markdown(f"你輸入的數字是：{number}")
```

* `step=1` 表示只能輸入整數。
* `min_value` 和 `max_value` 是最小值和最大值。

---

### ② 成績等級判斷

輸入成績後會顯示你的成績等級（A到F）：

```python
x = st.number_input("請輸入成績", step=1, min_value=0, max_value=100)
y = "?"

if x < 60:
    y = "F"
elif 60 <= x < 70:
    y = "D"
elif 70 <= x < 80:
    y = "C"
elif 80 <= x < 90:
    y = "B"
else:
    y = "A"

st.markdown(f"你的等級是：{y}")
```

* 使用 `if`、`elif` 判斷輸入的成績，來決定等級。

---

### ③ 按鈕練習（button）

按按鈕後會發生特別效果：

```python
st.markdown("### 按鈕練習")

if st.button("放氣球🎈", key="balloons"):
    st.balloons()

if st.button("下雪❄️", key="snow"):
    st.snow()
```

* `st.button()` 按下去之後會執行裡面的動作（放氣球或下雪）。

---

# 二、for迴圈

讓電腦做重複的動作：

```python
for i in range(5):
    print(i)  # 會印出 0,1,2,3,4
```

### 其他用法：

* `range(1, 5)` → 從1開始到4結束（不含5）

  ```python
  for i in range(1, 5):
      print(i)  # 1,2,3,4
  ```

* `range(1, 10, 2)` → 從1開始，每次增加2，到9結束

  ```python
  for i in range(1, 10, 2):
      print(i)  # 1,3,5,7,9
  ```

---

# 三、數字金字塔（練習題）

用輸入數字來畫出數字金字塔：

```python
number = st.number_input("數字", step=1, min_value=1, max_value=9)
st.markdown("數字金字塔:")

for i in range(1, number + 1):
    x = str(i)
    st.write(x * i)
```

* 假設輸入3，會印出：

```
1
22
333
```

---

# 四、列表 (list)

可以存放很多不同的東西：

```python
a = [90, 50, 20, 80, 70]
print(a[0])  # 90，第一個東西
```

* 列表中第一個東西的編號（index）是從0開始算的。

### 列表的切片

取列表中的一小段：

```python
name = ["合合", "小明", "小美", "幕幕", "黑黑"]
print(name[2:5])  # 從第2到第4個（不含第5個）→ ["小美", "幕幕", "黑黑"]
```

* `[::2]` 從頭到尾，每隔一個取一次。
* `[1:4]` 從第1個取到第3個。

---

# 五、列表長度、走訪

用 `len()` 看列表有幾個東西：

```python
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6
```

用 `for` 走訪列表中每一個東西：

```python
for i in L:
    print(i)  # 依序印出1,2,3,"a","b","c"
```

---

# 六、變數的複製方式

變數有兩種複製方法：

### ① 複製值（call by value）

數字的複製：

```python
a = 1
b = a
b = 2
print(a, b)  # 1, 2 (a沒變)
```

### ② 複製位置（call by reference）

列表的複製：

```python
a = [1, 2, 3]
b = a
b[0] = 2
print(a, b)  # [2,2,3], [2,2,3] (a會跟著變)
```

如果不想讓原本的變數也跟著變，要用`.copy()`：

```python
a = [1, 2, 3]
b = a.copy()
b[0] = 2
print(a, b)  # [1,2,3], [2,2,3] (a沒變)
```

---

# 七、列表增加和移除元素

### 增加元素：

```python
L = [1,2,3]
L.append(4)  # [1,2,3,4]
```

### 移除元素：

* 移除指定值（`remove`）：

  ```python
  L = ["a","b","c","a"]
  L.remove("a")  # 移除第一個"a"，變["b","c","a"]
  ```

* 移除指定位置（`pop`）：

  ```python
  L = ["a","b","c"]
  L.pop(0)  # 移除第0個，變["b","c"]
  L.pop()   # 移除最後一個，變["b"]
  ```

---

# 八、練習題

### 算平均分數：

```python
midterm = [80, 95, 78, 60, 55]
final = [64, 73, 52, 34, 95]
avg = (midterm[1] + final[1]) / 2
print(avg)  # (95+73)/2=84
```

### 用for印出名單編號：

```python
name = ["Amy", "Mandy", "Peter"]
index = 1
for i in name:
    print(f"{index}號是{i}")
    index = index + 1

# 顯示：
# 1號是Amy
# 2號是Mandy
# 3號是Peter
```

---

以上就是今天學到的 Python 內容囉！多多練習，你會更厲害～😊

        """
    )
