# JavaScript概述

## 简介

JavaScript是一种**基于对象**和**事件驱动**并具有安全性能的**客户端**脚本语言。

基于对象：JavaScript不仅能创建新的对象，还能使用现有的对象。

事件驱动：用户在网页上例如移动鼠标、点击鼠标、按下键盘等操作引起的动作，该动作就是事件，可

能会引起事件响应。

脚本语言：传统编写语言需要经过编写-编译-链接-运行四个步骤，JavaScript作为脚本语言，只需要编

写和运行两个步骤。

客户端：运行在你我的电脑上。程序在客户端（浏览器）执行。

## 作用

浏览器中 JavaScript，用于与**用户交互**，以及实现页面中各种**动态特效**。

## JavaScript特点

动态类型：不用给变量指定数据类型。

弱类型：一个变量可以赋不同类型的值。

简单性：解释性语言，不需要编译，方便调试

必要性：主流浏览器统一支持的语言

跨平台性：JavaScript依赖于浏览器执行，与操作环境无关，只要能运行浏览器的计算机，就可以正确

执行。

## JavaScript基本用法

1. HTML文件内部 JavaScript 代码：将js代码写在script标签中。

```javascript
<script>
alert('我要吃辣子鸡！');
</script>
```

2. 外部 JavaScript 文件：将js代码写在外部js文件中，然后用script标签直接引入该文件。

index.js:

```javascript
prompt('这又是一个标题！');
```

demo1.html:

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initialscale=1.0">
<title>Document</title>
</head>
<body>
<script src="./js/index.js"></script>
</body>
</html>
```

请注意：1.**外部脚本文件中，不能含有 `<script>` 标签，只能含有 JavaScript 代码。 2.引入外部**

**文件时，HTML 文件的 `<script>` 标签中间不能写 JavaScript 代码；若同时有外部 JavaScript**

**文件引入与内部 JavaScript 代码，需要各自使用 `<script>` 标签！3.写成单独的 js 文件有利于网**

**页结构和行为的分离，且可以复用。**

3. 关于script标签放置的位置：
   1.`<script>`放在 `<head>`标签中，但是，如果你选择放在这里，请注意是否能获取到元素，

如果是外部js文件，解决方法1是向script标签添加defer属性。

    2.`<script>`放在 `<body>`的结束标签之前。
