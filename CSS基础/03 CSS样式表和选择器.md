# 1 CSS优点
 
  能使数据和显示分开，降低网络流量，使整个网站视觉效果一致，耦合性降低。
  
  html只提供数据和一些控件，完全交给CSS提供各种各样的样式
  
 # 2 CSS重点
   
   **盒子模型 浮动 定位**
   
 # 3 CSS整体感知
 
   ```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style type="text/css">  /*css的书写舞台*/
        p{   /*选择器{属性名：属性值}*/  
            color:red;
            font-size: 30px;
            text-decoration: underline;
            font-weight: bold;
            text-align: center;
            font-style: italic;
        }
        h1{
            color: blue;
            font-size: 50px;
            font-weight: bold;
            background-color: pink;
        }
    </style>
</head>
<body>
    <h1>我是大标题</h1>
    <p>
        我是内容
    </p>
</body>
</html>
   ```
# 4 CSS一些简单常见的属性

  字体颜色(c)color
  
  字号大小(fos) font-size
  
  背景颜色(bgc) background-color
  
  加粗(fwb) font-weight:bold;
  
  不加粗(fwn) font-weight: normal;
  
  斜体(fsi) font-style: italic;
  
  不斜体(fsn) font-style: normal;
  
  下划线(tdu) text-decoration: underline;
  
  没有下划线(tdn) text-decoration: none;
  
 # 4 CSS与html结合的方式
 ## 4.1 行内样式
   对于多个相同标签的同一样式定义比较麻烦，只针对于此标签使用 
   ```
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>洗白白</p>
    <p style="color:red">你懂的</p>
    <p style="color:white; background-color: red;">我不会这样轻易的狗带</p>
</body>
</html>
   ```
 ## 4.2 内嵌样式表
 
  
  
