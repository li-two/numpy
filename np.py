# coding:utf-8
import numpy as np

a = np.array([1, 2, 3, 4])                    #构造数组
print(a.shape) 

b = np.array([[1, 2, 3, 4],[1, 2, 3, 4]])                    #构造数组
print(b.shape) 

c = np.array([[[1, 2, 3, 4],[1, 2, 3, 4]],[[1, 2, 3, 4],[1, 2, 3, 4]]])                    #构造数组
print(c.shape) 


# 用0作为占位符
d = np.zeros((2,2))
print(d)

# 用1作为占位符

e = np.ones((1,3))
print(e)

f = np.full((3,3),5) 
print(f)

g = np.eye(2)
print(g)

h = np.random.random((2,2))
print(h)

i = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(i.shape)
j = i[:2 ,1:3]
print(j)
print(i[0,1])
j[0,0] = 77
print(i[0,1])

k = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(k) 
l = np.array([0, 2, 0, 1])
print(k[np.arange(4), l])
k[np.arange(4), l] += 10
print(k)

# 数组的加减乘除
print('*'*30)
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x + y)
print(np.add(x, y))
print('*'*30)
print(x - y)
print(np.subtract(x, y))
print('*'*30)
print(x * y)
print(np.multiply(x, y))
print('*'*30)
print(x / y)
print(np.divide(x, y))

print(np.sqrt(x))

# 数组的转至
print('*'*30)

x = np.array([[1,2,3], [3,4,5]])
print(x)    
print(x.T)  
print('*'*30)
v = np.array([1,2,3])
print(v)
print(v.T)

# 给一排加一个数字
print('*'*30)
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)
for i in range(4):
    y[i, :] = x[i, :] + v
print(y)
# 同上面的方法一样的,用的是直接加上一个数字
print('*'*30)
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))  
print(vv) 
y = x + vv 
print(y)

print('*'*30)
v = np.array([1,2,3])
w = np.array([4,5])  
print(np.reshape(v, (3, 1)) * w)
print('*'*30)
x = np.array([[1,2,3], [4,5,6]])

print(x + v)
print('*'*30)
print((x.T + w))
print('*'*30)
print(x + np.reshape(w, (2, 1)))

print('*'*30)
print(x * 2)
s = np.reshape(w, (2, 1))
ss = w.reshape(-1,1)
print(s)
print(ss)