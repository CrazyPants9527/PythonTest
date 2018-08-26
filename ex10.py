import datetime
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)
#1.python转义字符有：
# \(在行尾)------->续行
#\\---->\   \'\"------>'""
# \a--->响铃   \b---->退格 \e---->转义
# \n--->转行    \v--->纵向制表符    \t----->横向制表符
# \r--->回车    \f--->换页
#\oyy 	八进制数yy代表的字符，例如：\o12代表换行
#\xyy 	十进制数yy代表的字符，例如：\x0a代表换行
#\other 	其它的字符以普通格式输出

#%r和%s区别
print("-"*30)

print ("I am %d years old." % 22)
print ("I am %s years old." % 22)
print ("I am %r years old." % 22)
#小结：%r处理对象为int等数据类型时无区别
text = "I am 22 years old." 
print ("I said: %s." % text)
print ("I said: %r." % text)
#小结：%r处理对象为str变量时，加‘’
d = datetime.date.today()
print ("%s" % d)
print ("%r" % d)
#小结：%r能重现它所代表的对象