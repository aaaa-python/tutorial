# -*- coding: utf-8 -*-

print(2 + 2)  #4
print(50 - 5*6) # 20
print((50-5*6) / 4) # 5.0
print(8 / 5) #1.6

print(17 / 3) #5.666666666666667
print(17 // 3) #5
print(17 % 3) #2
print(5*3 + 2) #17

print(5 ** 2) #25
print(2 ** 7) #128

width = 20
height = 5*9
print(width * height)

print(3*3.75 / 1.5) #7.5
print(7.0 / 2) #3.5

tax = 12.5 / 100
price = 100.50

_ = price * tax
print(_)
_ = price + _
print(_)
print(round(_, 2))

print('spam eggs')
print('doesn\'t')
print("doesn't")
print('"Yes", he said.')
print('\"Yes\", he said.')
print('"Isn\'t," she said.')
a = '"Isn\'t," she said.'
print(a)

print('Firstline.\nSecond line.')

print(r'C:\some\name')

print("""\
    Usage: thingy [OPTIONS]
        -h
        -H hostname
    """)\

print(3 * 'un' + 'ium')
print('Py' 'thon')

text = ('今日はいい天気ですね'
        '明日も元気です。')
print(text)

prefix = 'Py'
print(prefix + 'thon')
print(prefix[0])
print(prefix[1])
print(prefix[-1])
print(prefix[0:2])
print(prefix[1:2])
print(prefix[:2])
print(prefix[1:])
print(prefix[0:])
print(prefix[-2:])
prefix2 = prefix[:2] +'py'
print(prefix2)
print(len(prefix2))