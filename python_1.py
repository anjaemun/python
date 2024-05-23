Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:47) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = 10
>>> if n%2 == 0
SyntaxError: expected ':'
>>> if n%2 == 0;
SyntaxError: invalid syntax
>>> if n%2 == 0:
...     print('even')
...     print('짝수')
... else:
...     print('odd')
...     print('홀수')
... 
...     
even
짝수
>>> print(n)
10
>>> a = 3;
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(a+b)
NameError: name 'b' is not defined
>>> print(n+a)
13
>>> a = 2
>>> print(n+a)
12
