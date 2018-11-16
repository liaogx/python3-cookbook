#数字的格式化输出，如位数、对齐、千位分隔符和其他细节。format()函数
x = 1234.56789
print(format(x,'>10.1f'))
print(format(x,'10.2f'))
print(format(x,','))
print(format(x,'0,.1f'))
print(format(x,'e'))
print(format(-x,'0.2E'))

#包含千位符的格式化跟本地化没有关系。 如果你需要根据地区来显示千位符，你需要自己去调查下 locale 模块中的函数了。 你同样也可以使用字符串的 translate() 方法来交换千位符。比如：
swap_separators = {ord('.'):',',ord(','):'.'}
print(format(x,',').translate(swap_separators))
#为什么会输出'1.234,56789'
#在很多Python代码中通常会看到使用%来格式化数字，如：
print('%0.2f' % x)
print('%10.1f' % x)
print('%-10.1f' % x)

#这种格式化方法也是可行的，不过比更加先进的format()要差一点。
#比如，在使用%操作符格式化数字的时候，一些特性(添加千位符)并不能被支持。







