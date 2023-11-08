## CSS基本样式修饰

## 字体样式

### 字体系列

属性：font-family

功能：设置元素的字体，可以设置多个字体，当前面的字体不存在时，则会自动使用后面的字体。

使用方法：

```html
font-family: '仿宋';
font-family: '黑体','仿宋';
```

### 字体大小

属性：font-size

功能：设置元素的字体大小，单位有px（像素），%、em（相对于父元素字体大小），rem（相对于

html元素字体大小），默认字体大小为16px，请注意，浏览器一般存在字体大小最小限制，不同浏览

器，可能存在不同。

使用方法:

```html
font-size:30px;
font-size:2em;
font-size:200%;
font-size:2rem;
```

### 字体风格

属性：font-style

功能：设置字体斜体显示；**属性值有normal、italic、oblique；**关于italic与oblique，italic是使用字

体的斜体，即必须要求字体包含斜体，否则无效，而oblique是倾斜显示，无论字体是否包含斜体，都

可以倾斜显示，但是，有些情况下，oblique的效果不如italic，所以优先使用italic，如果字体没有斜

体，再使用oblique。

使用方法：

```html
font-style: italic;
font-style: oblique;
```

### 字体粗细

属性：font-weight

功能：设置字体粗细，属性值有关键字和数字两种：

1. 关键字：lighter（比默认值细）、normal（默认值）、bold（粗体）、bolder（加粗）。
2. 数字：100~900之间的整百数，400等于normal，700等于bold。

**请注意**，一个字体支持的字体粗细可能是有限的，如果你设置了一个不支持的字体粗细，那么它将会根

据以下方法进行调整：

* 如果指定的权重值在400和500之间（包括 400和500）：
  * 按升序查找指定值与 500 之间的可用权重；
  * 如果未找到匹配项，按**降序**查找小于指定值的可用权重；
  * 如果未找到匹配项，按**升序**查找大于 500 的可用权重。

+ 如果指定值小于 400 ，按**降序**查找小于指定值的可用权重。如果未找到匹配项，按**升序**查找大于指定值的可用权重（先尽可能的小，再尽可能的大）。
+ 如果指定值大于 500 ，按**升序**查找大于指定值的可用权重。如果未找到匹配项，按**降序**查找小于指定值的可用权重（先尽可能的大，再尽可能的小）。

  以上策略意味着，如果一个字体只有 normal 和 bold 两种粗细值选择，指定粗细值为 100-500 时，

实际渲染时将使用 normal ，指定粗细值为 501-900 时，实际渲染时将使用 bold 。

使用方法：

```html
font-weight:bold;
font-weight:700;
```

### 字体综合属性

属性：font

功能：在一个声明中设置所有属性，请注意，font属性中，我们这节课学习的四个属性可以分为两组，

A组：font-size和font-family，B组：font-style和font-weight，A组的属性是必须的，且组内前后相对

顺序不可变；B组不是必须的，组内的前后顺序也是可以调整的，但是，要注意的是，B组的位置在A组

的前面。

使用方法：

```html
font: italic bold 36px '宋体';
font: italic 700 36px '宋体';
font: italic bold 36em '宋体';
font: italic bold 36rem '宋体';
font: italic bold 36px '黑体','宋体';
font: bold 36px '宋体';
font: italic 36px '宋体';
font: 36px '宋体';
```

### 文本样式

### 文本缩进

属性：text-indent

功能：设置段落元素第一行缩进。

使用方法：

```html
text-indent:2em;
text-indent:-2em;
text-indent:20px;
```

推荐将缩进设置成相对值，这种方式可以保证不论文字字号为多大，始终能够缩进大小为2个文字的位

置。

### 文本对齐

属性：text-align

功能：设置元素文本行的对齐方式；常用属性值有left（左对齐）、center（居中）、right（右对

齐）。

使用方法：

```html
text-align: right;
```

### 文本修饰

属性：text-decoration

功能：设置文本修饰，可以添加下划线、删除线等；常用属性值有none（无装饰）, overline（上划

线）, underline（下划线），line-through（删除线）。

使用方法：

```html
text-decoration:underline;
```

### 行高

属性：line-height

功能：设置行与行之间的距离；属性值的单位有**px**（绝对值）、**em**（相对值，相对于当前字号大

小）；一般行高是文字的1.5倍。

使用方法：

```html
line-height: 30px;
line-height: 3em;
```

### 文本颜色

属性：color

功能：设置文字颜色；属性值可以是关键词，也可以是十六进制表示法，也可以是rgb表示；十六进制

表示法开头为 # , # 后面为三位或六位十六进制数字，三位是六位的缩写版本，表示每两位都是一个相同

的数字；rgb表示法每一位取值为 0~255 ，分别表示红、绿、蓝的比例；rgba相较于rgb加入了alpha通

道，表示透明度，透明度取值范围为 0~1 。

使用方法：

```html
/* 以下都是黑色 */
color: black;
color: #000;
color: #000000;
color: rgb(0, 0, 0);
color: rgba(0, 0, 0, 1);
```

# 超链接样式设置

超链接有四种状态：未被访问的超链接(:link)、访问过的超链接(:visited)、鼠标经过的超链接(:hover)、

链接被点击的那一刻(:active)；可以利用伪类对超链接的四种不同状态下的样式进行设置，在设置超链

接的多种状态时(>=2)，要使用特定顺序进行设置(:link、:visited、:hover、:active)。

使用方法：

```html
a:link {
color: red;
}
a:visited {
color: purple;
}
a:hover {
color: yellow;
}
a:active {
color: yellowgreen;
}
p {
color: rgba(50, 50, 50, 0.5);
}
p:hover {
color: white;
}
```

# 背景样式的设置

属性：background-color

功能：设置背景颜色；元素默认背景颜色是透明；属性值可以是关键词，也可以是十六进制表示法，也

可以是**rgb**表示；十六进制表示法开头为 # , # 后面为三位或六位十六进制数字，三位是六位的缩写版

本，表示每两位都是一个相同的数字；**rgb**表示法每一位取值为 0~255 ，分别表示红、绿、蓝的比例；

rgba相较于rgb加入了alpha通道，表示透明度，透明度取值范围为 0~1 。

使用方法:

```html
background-color: black;
background-color: #000;
background-color: #000000;
background-color: rgb(0, 0, 0);
background-color: rgba(0, 0, 0, 1);
```
