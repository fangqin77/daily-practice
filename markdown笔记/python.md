# 1 数据类型

## 1.1 数值型

* Python支持大数运算和存储

  $\circ$ 能够表示的数值种类：

  $\circ$ 十进制整数：100，-123

  $\circ$ 八进制整数：0o17 （对应十进制15）

  $\circ$ 十六进制整数：0x17（对应十进制23）0x2B（对应十进制43）

  $\circ$ 浮点数（小数）：3.14，0.125
* 支持的运算：

  $\circ$ +，-，*，/

  $\circ$ //（整除），**（指数运算，次幂），%（取余，模运算）

  $\circ$ ()（优先级运算符，提升运算优先级）

```python
a = 100
print(a) # 100
a = 0o17
print(a) # 15
a = 0x17
print(a) # 23
a = 0x2b
print(a) # 43
a = 3.14
print(a) # 3.14
```

```python
a = 10
b = 3
print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(a / b) # 3.333333...
print(a // b) # 3
print(a ** b) # 1000
print(a % b) # 1
```

```python
a = -10
b = 3
print(a // b)
print(a % b)
# Python -10 % 3 -> 2
# C -10 % 3 -> -1
# Python -10 // 3 -> -4
# C -10 / 3 -> -3
# Python 与 C C++ Java 整除结果不一致原因是取整方向不同
# Python 向负无穷取整
# C 向0取整
# a ÷ b = c ... d
# d = a - b × c
```

```python
import random
# 2023015756 ~ 2023015855
a = random.randint(0, 99)
a = a + 2023015756
print(a)
a = random.randint(2023015756, 2023015855)
print(a)
```

## 1.2 布尔类型

* 布尔类型的取值只有：**True** 和 **False**
* 关系运算：**>，<，>=，<=，==，!=**
* 逻辑运算：**and，or，not**

```python
print(10 > 9) # True
print(10 < 9) # False
print(10 == 9) # False
print(10 != 9) # True
a = 5
print(a > 1 and a < 10) # True
print(1 < a < 10) # 效果等同上一行，Python独有写法
print(a < 1 or a > 10) # False
print(not(1 <= a <= 10)) # False
print(a % 2 == 0) # False
print(a % 2 == 1) # True
print(a % 5 == 0) # True
```

## 1.3 列表

* 序列：有顺序编号的结构称之为序列

  $\circ$ 列表

  $\circ$元组

  $\circ$字符串
* 索引可以是正的，从左到右，从前到后，正向的顺序。是从**0**开始，合法的索引范围为**0 ~ N-1**
* 索引也可以是负的，从右到左，从后到前，反向的顺序。是从**-1**开始，合法的索引范围为**-1 ~ -N**
* 列表是序列的一种
* 列表的定义声明形式：

  $\circ$ `L = []` # L是一个空的列表

  $\circ$ `L = [1, 2, 3, 4]` # L是一个列表，里面元素有1,2,3,4

  $\circ$ 列表中的元素是使用空格隔开的

```python
L = [1, 2, 3, 4]
print(L) # [1, 2, 3, 4]
print(L[0]) # 1
print(L[1]) # 2
print(L[2]) # 3
print(L[3]) # 4
# print(L[4]) # IndexError: list index out of range
```

```python
L = [1, 2, 3, 4]
print(L[-1]) # 4
print(L[-2]) # 3
print(L[-3]) # 2
print(L[-4]) # 1
```

```python
L = [1, 2, 3, 4]
print(L) # [1, 2, 3, 4]
L[1] = 22
print(L) # [1, 22, 3, 4]
```

```python
L = [100, 3.14, "hello", True, [1, 2, 3]]
print(L[0]) # 100
print(L[1]) # 3.14
print(L[2]) # hello
print(L[3]) # True
print(L[4]) # [1, 2, 3]
print(L[4][2]) # 3
```

* 序列的分片操作

  $\circ$`序列名[start : stop : step]`

  $\circ$`start`：开始位置

  $\circ$`stop`：停止位置，截取的最后一个元素不包含stop

  $\circ$`step`：步长，每取一个元素向后移动几个元素。如果步长缺省，默认步长为1

```python
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L[0:5:1]) # [1, 2, 3, 4, 5]
print(L[0:5]) # [1, 2, 3, 4, 5]
print(L[:5]) # [1, 2, 3, 4, 5]
print(L[5:10]) # [6, 7, 8, 9, 10]
print(L[5:]) # [6, 7, 8, 9, 10]
print(L[0::2]) # [1, 3, 5, 7, 9]
print(L[1::2]) # [2, 4, 6, 8, 10]
print(L[-2::-2]) # [9, 7, 5, 3, 1]
print(L[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```

* 序列的一些基本操作

  $\circ$`序列 + 序列 `：将两个列表合并为一个列表

  $\circ$`序列 * 正整数` ：将序列重复拼接指定次数

```python
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3) # [1, 2, 3, 4, 5, 6]
L4 = L1 * 3
print(L4) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

* 列表的一些常用方法

```python
L1 = [1, 2, 3]
L1.append(4) # 在列表末尾添加新的元素
print(L1) # [1, 2, 3, 4]
```

```python
L1 = [1, 2, 3, 4]
L2 = L1 # 给L1列表起了一个名字叫L2
print(L2) # [1, 2, 3, 4]
L2[1] = 22
print(L2) # [1, 22, 3, 4]
print(L1) # [1, 22, 3, 4]
L1 = [1, 2, 3, 4]
L2 = L1[:] # 通过对L1列表分片得到一个新的列表，起名L2
print(L1) # [1, 2, 3, 4]
print(L2) # [1, 2, 3, 4]
L2[1] = 22
print(L1) # [1, 2, 3, 4]
print(L2) # [1, 22, 3, 4]
L1 = [1, 2, 3, 4]
L2 = L1.copy() # 给L1列表拷贝一份，起名L2
print(L1) # [1, 2, 3, 4]
print(L2) # [1, 2, 3, 4]
L2[1] = 22
print(L1) # [1, 2, 3, 4]
print(L2) # [1, 22, 3, 4]
```

```python
L1 = [1, 2, 2, 3, 2, 3, 2, 2, 2]
num = L1.count(2) # 统计L1列表中2这个元素的数量
print(num) # 6
```

```python
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L1 = L1 + L2
print(L1) # [1, 2, 3, 4, 5, 6]
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L1.extend(L2) # 将L2列表拼接到L1的后面
print(L1) # [1, 2, 3, 4, 5, 6]
```

```python
L = [1, 2, 5, 6]
L.insert(2, 3) # 在列表L中索引2位置插入元素3
print(L) # [1, 2, 3, 5, 6]
L.insert(3, 4)
print(L) # [1, 2, 3, 4, 5, 6]
L = [1, 2, 5, 6]
L.insert(3, 4)
L.insert(2, 3)
print(L) # [1, 2, 3, 5, 4, 6]
```

```python
L = [1, 2, 3, 4, 5, 6]
L.pop(1) # 将L列表索引为1的元素弹出
print(L) # [1, 3, 4, 5, 6]
```

```python
L = [1, 2, 3, 2, 5, 2]
L.remove(2) # 按照正向方向移出列表L中第一个出现的元素2
print(L) # [1, 3, 2, 5, 2]
```

```python
L = [1, 2, 3, 2, 5, 2]
L.clear() # 将列表L清空
print(L) # []
```

```python
L = [1, 2, 3, 4, 5, 6]
L.reverse()
print(L) # [6, 5, 4, 3, 2, 1]
L = [1, 2, 3, 4, 5, 6]
L = L[-1::-1]
print(L) # [6, 5, 4, 3, 2, 1]
```

* Python中的一些通用操作

  $\circ$len()：求序列中元素的个数

  $\circ$max()：求序列中元素的最大值

  $\circ$min()：求序列中元素的最小值

```python
L = [1, 4, 2, 7, 9, 5]
print(len(L)) # 6
print(max(L)) # 9
print(min(L)) # 1
```

## 1.4 元组

* 元组：可以理解成是不能修改的列表

```python
L = (1, 3, 5, 2, 4, 6)
print(L)
print(max(L))
# L[2] = 55 # TypeError: 'tuple' object does not support item assignment
```

## 1.5 字符串

* 字符串：字符组成的串
* 字符串的表示形式：

  $\circ$双引号形式：`"abcd"`

  $\circ$单引号形式：`'abcd'`

```python
print("hello")
print('hello')
print('hel"lo')
print("hel'lo")
print("he\"l\'lo")
print("hel\nlo")
print("hel\rlo")
print("hel\tlo")
print("he\tllo")
print("h\tello")
print("he\\\"llo")
```

* Python中如何输入数据：input()

  $\circ$`input()`：在命令行窗口读取一行输入内容作为字符串

  $\circ$`int()`：将字符串转换为整型数值

  $\circ$`float()`：将字符串转换为浮点数数值

  $\circ$`str()`：将数值转换为字符串

```python
s = input() # 从命令行读取一行内容作为字符串赋值给s
print(s) # 打印s的内容
```

```python
a = input() # a = "11"
b = input() # b = "22"
print(a+b) # 1122
```

```python
a = input() # a = "11"
b = input() # b = "22"
a = int(a) # a = 11
b = int(b) # b = 22
print(a+b) # 33
```

```python
a = int(input())
b = int(input())
print(a+b)
```

```python
a = int(input("请输入第一个数:"))
b = int(input("请输入第二个数:"))
print("两数之和为：" + str(a+b))
```

* Python中如何输出数据：print()

  $\circ$ print()：将数据打印到命令行中

  $\circ$ print()函数会在数据打印完成后自动打印一个换行符\n

  $\circ$ print()格式化输出：

  ->print("格式化字符串" % (待填入的数据列表))

  ->%s：将数据作为字符串填入

  ->%d：将数据作为整数填入

  ->%f：将数据作为浮点数填入

  ->如果不确定应该使用哪个格式转换说明符，那就使用%s

```python
print("ab")
print("ab", end="\n")
print("----------")
print("ab", end="")
print("cd")
print("张三", end="!!!!")
```

```python
names = ["张三", "李四", "尼古拉斯赵四", "刘能"]
nums = [50, 100, 1000000, 5]
for i in range(4):
print("%s，我秦始皇，V我%d" % (names[i], nums[i]))
```

* 字符串的常用方法

```python
s = "abcd1234"
print(s.find("123")) # 4
print(s.find("cd")) # 2
print(s.find("d")) # 3
print(s.find("zhangsan")) # -1
```

```python
s = "aabbaaccaaa"
s = s.strip("a") # 去掉s字符串首尾的"a"
print(s) # bbaacc
name = input("请输入姓名：")
name = name.strip(" ")
print("%s你好，再见" % (name))
```

```python
s = "ZhangSan"
s = s.upper() # ZHANGSAN
print(s)
s = "ZhangSan"
s = s.lower()
print(s) # zhangsan
s = "ZhangSan"
s = s.swapcase()
print(s) # zHANGsAN
```

```python
s = "hello, lisi!"
print(s) # hello, lisi!
s = s.replace("lisi", "zhangsan") # 将s中的"lisi"替换为"zhangsan"
print(s) # hello, zhangsan!
```

```python
s = "1,2,3,4,5,6"
L = s.split(",") # 将s根据","分割成一个列表
print(L) # ['1', '2', '3', '4', '5', '6']
s = ",".join(L)
print(s) # 1,2,3,4,5,6
```

```python
# 请输入一个加法表达式：1+2
# 1+2的结果为：3
# 请输入一个加法表达式：3+4
# 3+4的结果为：7
s = input("请输入一个加法表达式：") # "1+2"
L = s.split("+")
print("%s的结果为：%s" % (s, int(L[0])+int(L[1])))
```

## 1.6 字典

* 存储 `键-值`对的数据容器

```python
m = {"015765": "张三", "015777": "张小三", "015711": "张大三"}
print(m["015777"])
print(m["015711"])
# 如果键存在，则进行修改
m["015765"] = "张中三"
print(m)
# print(m["015700"])
# 如果键不存在，则进行添加
m["015700"] = "张巨三"
print(m)
```

---

# 2 流程控制语句

## 2.1 赋值语句

* `=`：将 `=`右侧表达式的值赋值给左侧的变量，`=`称之为赋值运算符。

```python
# a = 10
# b = 20
a, b = 10, 20
print(a) # 10
print(b) # 20
# t = a
# a = b
# b = t
a, b = b, a
print(a) # 20
print(b) # 10
```

## 2.2 if语句（分支语句）

```python
if <条件1>:
<语句块1>
elif <条件2>:
<语句块2>
elif <条件3>:
<语句块3>
...
else:
<语句块n>
```

* 实际开发中，根据实际需求来编写if语句

  $\circ$ if分支有且仅能有1个

  $\circ$ elif分支可以有任意多个 [0, n]

  $\circ$ else分支可以有0或1个

```python
num = int(input("请输入一个正整数："))
if num % 2 == 0:
print("偶数")
else:
print("奇数")
```

```python
# 输入1-7中的一个数字，输出对应星期（星期一、星期二、..、星期日）
num = int(input())
m = {1: "星期一", 2: "星期二", 3: "星期三", 4: "星期四", 5: "星期五", 6: "星期六", 7: "星期
日"}
print(m[num])
if num == 1:
print("星期一")
elif num == 2:
print("星期二")
elif num == 3:
print("星期三")
elif num == 4:
print("星期四")
elif num == 5:
print("星期五")
elif num == 6:
print("星期六")
else:
print("星期日")
```

```python
# 输入一个1~100的分数，判断其对应等级
# [90, 100] 优
# [70, 89] 良
# [60, 69] 中
# [0, 59] 差
num = int(input("请输入您的成绩(0~100)："))
if 90 <= num:
print("优")
elif 70 <= num:
print("良")
elif 60 <= num:
print("中")
else:
print("差")
# if 90 <= num <= 100:
# print("优")
# elif 70 <= num < 90:
# print("良")
# elif 60 <= num < 70:
# print("中")
# else:
# print("差")
# if num >= 90 and num <= 100:
# print("优")
# elif num>= 70 and num < 90:
# print("良")
# elif num >=60 and num <70:
# print("中")
# else:
# print("差")
```

```python
# 输入一个年份，判断其是否为闰年
# 2023 平年
# 2020 闰年
# 2000 闰年
# 1900 平年
y = int(input("请输入一个年份："))
if y % 100 == 0:
if y % 400 == 0:
2.3 while语句
while语句是一种循环语句
一般形式：
首先<条件>是否成立，则执行<循环语句块>，然后继续判断<条件>。当<条件>不成立时，循环结
束。
continue：立即停止本次循环，执行下一次循环，跳转到循环<条件>判断位置
print("世纪闰年")
else:
print("平年")
else:
if y % 4 == 0:
print("普通闰年")
else:
print("平年")
if y % 100 != 0 and y % 4 == 0:
print("普通闰年")
elif y % 400 == 0:
print("世纪闰年")
else:
print("平年")
```

## 2.3 while语句

* while语句是一种循环语句
* 一般形式：

```python
while <条件>:
<循环语句块>
```

* 首先<条件>是否成立，则执行<循环语句块>，然后继续判断<条件>。当<条件>不成立时，循环结

束。

```python
# 打印1~100所有的整数
num = 1
while num <= 100:
print(num)
num = num + 1
```

```python
# 打印1~100所有的偶数
# num = 1
# while num <= 100:
# if num % 2 == 0:
# print(num)
# num = num + 1
num = 2
while num <= 100:
print(num)
num = num + 2
```

* `continue`：立即停止本次循环，执行下一次循环，跳转到循环<条件>判断位置

```python
# 打印1~100所有的偶数
num = 1
while num <= 100:
if num % 2 != 0:
num = num + 1
continue
print(num)
num = num + 1
```

* `break`：直接结束整个循环的执行，跳出整个循环，执行循环之后的代码

```python
num = 2
while True:
print(num)
num = num + 2
if num > 100:
break
```

```python
# 打印水仙花数
# 在三位数中 100 ~ 999 之间，如果一个数字满足下面条件：
# abc = a*a*a + b*b*b + c*c*c
# 153 = 1*1*1 + 5*5*5 + 3*3*3
# 我们就称它为水仙花数
# num = 100
# while num < 1000:
# a = num // 100
# b = num // 10 % 10 # b = num % 100 // 10
# c = num % 10
# # if num == a*a*a + b*b*b + c*c*c:
# if num == a**3 + b**3 + c**3:
# print(num)
# num = num + 1
a = 1
while a < 10:
b = 0
while b < 10:
c = 0
while c < 10:
num = a * 100 + b * 10 + c
if num == a**3 + b**3 + c**3:
print(num)
c = c + 1
b = b + 1
a = a + 1
```

```python
# 给定a和b两个正整数，求他们的最小公倍数
# s = input() # 4,6
# L = s.split(",") # ["4", "6"]
# a = int(L[0]) # 4
# b = int(L[1]) # 6
a, b = map(int, input().split(","))
c = max(a, b)
while True:
if c % a == 0 and c % b == 0:
print(c)
break
c = c + 1
```

```python
# 给定a和b两个正整数，求他们的最大公约数
a, b = map(int, input().split(","))
c = min(a, b)
while True:
if a % c == 0 and b % c == 0:
print(c)
break
c = c - 1
```

## 2.4 for语句

* for循环通常是在确定循环执行次数的情况下使用的
* while循环通常是在不确定循环执行次数的情况下使用的
* for循环 和 while循环 是可以互相转换的
* 一般形式：

```python
for <循环变量> in <迭代器对象>:
<循环语句块>
```

使用 `<循环变量>`依次去取 `<迭代器对象>`中的每一个元素，每取依次，执行一遍 `<循环语句块>`

```python
L = [11, 22, 33, 44, 55, 66, 77]
for num in L:
print(num)
s = "HelloWorld!"
for c in s:
print(c)
```

* range()函数

  $\circ$ range()函数可以产生一个迭代器对象

  $\circ$ range(start, stop, step)

```python
for i in range(1, 101, 1):
print(i)
for i in range(1, 101):
print(i)
```

```python
for num in range(100, 1000):
a = num // 100
b = num // 10 % 10
c = num % 10
if num == a**3 + b**3 + c**3:
print(num)
```
