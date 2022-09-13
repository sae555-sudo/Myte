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
 
   在head标签中加入<style>标签，对多个标签进行统一修改。对于局部不够灵活。
 ```
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style type="text/css">  /*内嵌样式表*/
        p{
            font-weight: bold;
            font-size: italic;
            color: red;
        }
        
    </style>
</head>
<body>
    <p>洗白白</p>
    <p style="color:blue">行内样式</p> 
</body>
</html>
 ```
 
## 4.3 引入外部样式表
 
 (1)<link>标签，<link rel="stylesheet" type="text/css" href="a.css"></link>
 
 (2)采用import，必须写在<style>标签中，而且必须是第一句   @import url(a.css);
 
 a.css中
 ```
 p {
    border: 1px solid red;
    font-size: 40px;
}
 ```
 html中:
 <link>标签的rel属性:stylesheet 定义的样式表  alternate stylesheet 候选的样式表； 使用alternate stylesheet可以给同一个标签定义好几种样式，并且可以在html中选择对应的样式
 ```
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="a.css"></link>
    <title>Document</title>
    
</head>
<body>
    <p>洗白白</p>
    <p style="color:blue">你懂的</p>
</body>
</html>
 ```
 # 5 CSS的四种基本选择器
 
 CSS选择器就是CSS要作用的标签，标签名称就是选择器，分为基本选择器和扩展选择器
 
 ## 基本选择器
 
 1. 标签选择器：针对一类标签
 
   用来描述共性，所有的标签都可以是选择器。比如ul li label dt dl input
   
   选择的是所有的，而不是一个
   ```
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            border: 1px solid red;
        }
        p{
            border: 2px solid blue;
        }
    </style>  
</head>
<body>
    <div>洗白白</div>
    <div>你懂的</div>
    <p>呵呵哒</p>
</body>
</html>
   ```
 
 2.ID选择器: 针对某个特定标签
 
 针对某一个特定的标签，只能使用一次
 
 html任何标签都可以有id属性，标签的名字可以任取，只能有字母、数字、下划线；必须以字母开头；不能和标签同名；一个页面上有一个id为pp的p，不能出现一个id为pp的div
 
 #mytitle{ border:3px dashed green; }
 
 ```
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        #mytitle{
            border: 3px dashed green;
        }
    </style>  
</head>
<body>
    <h1 id="mytitle">骑上蜗牛来追我呀</h1>
</body>
</html>
 ```
 
 3.类选择器：针对想要的所有标签
 
 .one{width:800px; }
  
  可以被多种标签使用；
  
  同一个标签可以使用多个类选择器，用空格隔开
  
  <h3 class="teshu zhongyao"></h3>
  
  ```
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
       .one{
        color: blue;
        font-size: 20px;
       }
    </style>  
</head>
<body>
    <div>洗白白</div>
    <div class="one">你懂的</div>
    <p class="one">呵呵哒</p>
</body>
</html>
  ```
  ```
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
       .lv{
        color: green;
       }
       .da{
        font-size: 30px;
       }
       .underline{
        text-decoration: underline;
       }
    </style>  
</head>
<body>
    <p class="lv da">段落1</p>
    <p class="lv">段落2</p>
    <p class="da underline">段落3</p>
</body>
</html>
  ```
  不要用一个类名把某个标签的所有样式写完。
  
  每一个类要尽可能小，有公共的概念，能让更多的标签使用。
  
  尽可能用class，除非极特殊情况可以用id。
 
 4.通配选择器：针对所有的标签都使用（不建议使用）
 
  ## 高级选择器
 
 后代选择器：用空格隔开
 
   空格表示后代，.div1 p 表示.div1的后代所有的p
   
   ```
   <style type="text/css">
    .div1 p {
        color: red;
    }
</style>
   ```
   
   定义了<h3>标签中的<b>标签中的<i>标签的样式，h3和b和i不一定是连续紧挨着的
   
   ```
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
       h3 b i{
        color: red;
       }
    </style>  
</head>
<body>
    <h3>我就是<b>那一只<i>披着羊皮的狼，</i>而你是</b>我的猎物</h3>
</body>
</html>
   ```
   
 
 交集选择器：选择器之间紧密相连
 ```
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
       h3.special{
        color: red;
       }
    </style>  
</head>
<body>
    <h3 class="special zhongyao">标题1</h3>
    <h3 class="special">我也是标题</h3>
    <p>我是段落</p>
</body>
</html>
```
  交集选择器没有空格，div.red和div .red是两个意思
 
 并集选择器：用逗号隔开
 
 伪类选择器
 
  # 6 CSS3的一些选择器
  
  1.子代选择器
  
  ```
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>      
        div > p{
            color:red;
        }
    </style>  
</head>
<body>
    <div>
        <p>我是div的儿子</p>
    </div>
    <!--子代选择器不能选择下面这个-->
    <div>
        <ul>
            <li>
                <p>我是div的重孙子</p>
            </li>
        </ul>
    </div>
</body>
</html>
  ```
  
  2.序选择器
  
  设置无序列表ul中的第一个li为红色
  
  ```
  <style type="text/css">
    ul li:first-child{
      color:red
    } 
  </style>
  ```
  
  3.下一个兄弟选择器
  
  选择h3后紧挨的第一个兄弟
  
  ```
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>      
      h3 + p{
        color: red;
      }
    </style>  
</head>
<body>
    <h3>我是一个标题</h3>
    <p>我是一个段落</p>
    <p>我是一个段落</p>
    <p>我是一个段落</p>
    <h3>我是一个标题</h3>
    <p>我是一个段落</p>
    <p>我是一个段落</p>
    <p>我是一个段落</p>
    <h3>我是一个标题</h3>
    <p>我是一个段落</p>
    <p>我是一个段落</p>
    <p>我是一个段落</p>
    <h3>我是一个标题</h3>
</body>
</html>
  ```
  
  
 
 

   
  
  
