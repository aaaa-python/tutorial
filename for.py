# -*- coding:utf-8 -*-

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)

for i in range(5):
    print(i)

print(range(5, 10))
print(range(0, 10, 3))

for i in range(5, 10):
    print(i)

for i in range(0, 10, 3):
    print(i)

for i in range(-10, -100, -30):
    print(i)
