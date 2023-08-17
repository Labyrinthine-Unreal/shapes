#a= 1/2b*h
#a=l*w
#a=1/2(b1+b2)h
#C=2*3.14*r
#a=3.14*r^2

'''Trapezoid'''
_ = .5
b1 = 265 
b2 = 120 
_b = b1+b2 
_b2 = _*_b
h = 45 
print(_b2*h)

'''Complex Squares'''
# p = b+b+(d-b)+c+d+(c+b) 
b = 6 
c = 8 
d = 12

_db = d-b
_ = b+b+_db+c+d 
_cb = c+b 
p = _+_cb 
print(p)
# a = b^2+(c*d)
# _ = b**2
# _cd = c*d 
# a = _+_cd
# print(a)

import numpy as np
'''Complex Triangles'''
# p = a+b+e+d
# a = (np.sqrt(3)*a^2//4) + 1/2*e*c 
a = 3
b=3
c=5 
d = 13 
e = 12
sqrt3 = np.sqrt(3) 
pow = sqrt3*a**2 
div = pow//4
add = .5*e*c 
print(div + add)

p = a+b+e+d 
print(p)


'''semi-circle/square'''
# p=(1/2*3.14*diameter)+(3*L)
# a=1/2*3.14*r^2+s^2 =>s->area = L*W

'''Complex Squares/Triangles (4 triangle bases on one square)'''
#   
#   _
# <|_|>

#p=c*a+c*b
#a=Look at Triangle = 1/2b*h
# a = 1/2
_ = .5 
a = 5 #hypotenuse
b = 3 #triangle height 
c=4 #Base of triangle / Length of square

_ca= c*a
_cb = c*b 
p = _ca+_cb 
print(p)


_cb = c*b 

a = _*_cb 
sqr = c**2 
_a = c*a 
_sqr = sqr 
_a_ = _a +_sqr
print(_a_)








