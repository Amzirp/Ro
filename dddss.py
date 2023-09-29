Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list = []
... count = 0
... num = 0
... 
... while count < 50:
...     if num % 2 == 0:
...         my_list.append(num)
...         count += 1
...     num += 1
... 
