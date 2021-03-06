# 55039669

"""
По условию задачи необходим было реализовать алгоритм вычисления из входных данных (строки)
арифметических операций методом польской нотации. При реализации алгоритма необходимо было использовать
стек.


--ПРИНЦИП РАБОТЫ--

Как и было сказано в условии задачи алгоритм необходимо было построить на стеке.

Был создан стек с методами push(value), pop().

Метод push(value) используется для добавления элемента в конец стека.

Метод pop() - для удаления и возврата элемента с конца стека, так как стек работает по принципу LIFO - последний
пришел, первый ушел.

Имопртируем модуль operator для создания арифметических операций.

Создаем словарь operators и записываем в него символы арифметических операций со значениями в value с методами
из модуля operator для проведения арифметических операций.

Функцией read_input() считываем входное значение, преобразуем его в список.

Функцией polish_notation(value) проходим циклом по элементам списка, который был создан в результате работы
функции read_input(), сравниваем и определяем какой элемент мы сейчас смотрим в цикле, если это не символ
арифметической операции, тогда записываем его в стек. Если же далее нам попадается символ арифметический
операции, то берем из стека два предыдущих элемента и удаляем их оттуда, при этом записываем их в переменные.
После этого совершаем над ними соответствующую арифметическую операцию путем обращения к соответствующему ключу
словаря operators и передаем значения двух ранее определенных переменных в соответсвующий метод модуля operator.
Результат арифметической операции записываем в стек.
Далее цикл продолжается, пока не закончатся все элементы списка.
В конце выводим результат работы алгоритма.


--ВРЕМЕННАЯ СЛОЖНОСТЬ--

Сложность работы стека составляет О(1). Сложность работы функции polish_notation(value) составляет О(n), так
как в работе мы используем цикл.
Получается, что весь алгоритм имеет сложность О(n).


--ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ--

В процессе работы алгоритма созается два списка фиксированного размера, поэтому их сложность явлется константной,
так же используется две переменных для проведения арифметических операций. И сложность так же является константной.
В стеке используется динамический массив и его размер зависит от входных данных. Сложность составляет О(n).

Общая пространственная сложность данного алгоритма составляет О(n).
"""

import operator

operators = {
    '*': operator.mul,
    '/': operator.floordiv,
    '+': operator.add,
    '-': operator.sub,
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def read_input():
    s_input = list(map(str, input().split()))
    return s_input


def polish_notation(s):
    stack = Stack()
    for i in s:
        if i not in operators:
            stack.push(i)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            stack.push(operators[i](b, a))
    return stack.items[-1]


if __name__ == '__main__':
    print(polish_notation(read_input()))
