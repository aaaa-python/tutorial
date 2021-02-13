# -*- coding:utf-8 =*-

square = [1, 4, 9, 16, 25]
print(square)

print(square[0])
print(square[3:])
print(square[-1])
print(square[:])
print(square + [36, 48, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)
cubes.append(216)
print(cubes)
cubes.append(7**3)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
print(len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0][1])
print(x[1][1])

i = 256*256
print("The value of i is", i)

#フィボナッチ級数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
