# -*- coding: utf-8 -*-

# for i in range(0):
#     print(i)
#     # if i > 5:
#     #     break
# else:
#     # выполняется когда в цикл не зашли или когда прошли по всем элементам
#     print('else branch')


try:
    # raise AssertionError()
    print('try block')
except AssertionError:
    print('catch AssertionError')
else:
    print('else block')