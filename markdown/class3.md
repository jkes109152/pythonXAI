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

- `step=1` 表示只能輸入整數。
- `min_value` 和 `max_value` 是最小值和最大值。

---

### ② 成績等級判斷

輸入成績後會顯示你的成績等級（A 到 F）：

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

- 使用 `if`、`elif` 判斷輸入的成績，來決定等級。

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

- `st.button()` 按下去之後會執行裡面的動作（放氣球或下雪）。

---

# 二、for 迴圈

讓電腦做重複的動作：

```python
for i in range(5):
    print(i)  # 會印出 0,1,2,3,4
```

### 其他用法：

- `range(1, 5)` → 從 1 開始到 4 結束（不含 5）

  ```python
  for i in range(1, 5):
      print(i)  # 1,2,3,4
  ```

- `range(1, 10, 2)` → 從 1 開始，每次增加 2，到 9 結束

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

- 假設輸入 3，會印出：

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

- 列表中第一個東西的編號（index）是從 0 開始算的。

### 列表的切片

取列表中的一小段：

```python
name = ["合合", "小明", "小美", "幕幕", "黑黑"]
print(name[2:5])  # 從第2到第4個（不含第5個）→ ["小美", "幕幕", "黑黑"]
```

- `[::2]` 從頭到尾，每隔一個取一次。
- `[1:4]` 從第 1 個取到第 3 個。

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

- 移除指定值（`remove`）：

  ```python
  L = ["a","b","c","a"]
  L.remove("a")  # 移除第一個"a"，變["b","c","a"]
  ```

- 移除指定位置（`pop`）：

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

### 用 for 印出名單編號：

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

以上就是今天學到的 Python 內容囉！多多練習，你會更厲害～ 😊
