#What is string?
honghapp = 'is delcious' #this is the string
mosiclab = "is using for making pasta" #this is also string
num = 163.163163163
#so we can understand the string as a sequence of characters that is treated as a single item
#and you can see the string is composed of single quotes or double qoutes
#then let's study about string
print(honghapp)
print(honghapp + mosiclab)
print(honghapp + "mosiclab")
print(honghapp*3)
#string can be plus and multiply, but it can't calculate minus or plus with just character-it must be print with charecter with quotes-
print(str("helloow")+str(mosiclab)) #it works! but if we use print(str(helloww)+str(mosiclab)), it can't print
print(int(num)+num)
#print(int(num)+mosiclab) ---> this is error!
print(mosiclab*int(num))
print(str(num)+mosiclab)
#so you can guess string can be calculated by its type

#if you want to handle the string, you must know 'postion of a character' identified with the numbers
print("I",honghapp[-6],mosiclab[10],"v","e","y",honghapp[8],"u")
#as you can see 21st code, 'is delicious' code has start with 0 identified charecter number and it can also see as -1 to~ if it is count its end
