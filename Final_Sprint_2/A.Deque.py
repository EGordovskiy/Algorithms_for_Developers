# 55041645

"""
По условию задачи необходимо было реализовать Дек с следующими методами:
- push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
- push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
- pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
- pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Так же по условию задачи, было необходимо реализовать эффективный Дек: чтобы все методы выполнялись за О(1).
Использовать реализацию на связном списке было запрещено.


--ПРИНЦИП РЕАЛИЗАЦИИ--

Дек по сути - это очередь с двумя концами. По условию задачи нам как раз было необходимо добавлять и извлекать
элементы с обоих концов.

Для реалзиации стека решил выбрать очередь, выполненную на кольцевом буфере.

В самом начале создал массив постоянно размера.

Методом push_back(value) добавляем элемент в конец дека. При этом указателем tail определяем, куда именно мы
добавляем элемент в конец дека. При добавлении элемента размер Дека увеличивается на одно значение.
Для метода pop_back() так же используется указатель tail, но уже в обратном направлении. Необходимо найти предыдущий
элемент перед tail, чтобы определить, какой-именно элемент необходимо удалить. Когда элемент найден, он удаляется,
ячейка массива заполняется значением None, а значение удаленного элемента выводится на печать. Размер Дека уменьшается
на одно значение.

Похожим образом реализованы два других метода.
Метод push_front(value) и метод pop_front() используют для добавления элемента в начало Дека
и удаления элемента из начала Дека соответственно. В качестве указателя используется указатель head (голова) Дека.
При добавлении элемента в начало Дека, head увеличивается на еденицу и размер Дека, тоже увиличивается на одно
значение. При удалении элемента из начала Дека, head и size (размер Дека) уменьшаются на единицу.


--ВРЕМЕННАЯ СЛОЖНОСТЬ--

Все методы Дека реализованы так, что временная сложность алгоритма составляет О(1).


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ--

При реализации Дека все операции проводятся на массиве постоянного размера, таким образом
алгоритм использует О(n) памяти.
"""


class Deque:
    def __init__(self, m):
        self.items = [None] * m
        self.head = 0
        self.tail = 0
        self.size = 0
        self.max_m = m

    def is_empty(self):
        return self.size == 0

    def push_front(self, item):
        if self.size != self.max_m:
            self.items[self.head] = item
            self.head = (self.head - 1) % self.max_m
            self.size += 1
        else:
            raise IndexError('size limit')

    def push_back(self, item):
        if self.size != self.max_m:
            self.tail = (self.tail + 1) % self.max_m
            self.items[self.tail] = item
            self.size += 1
        else:
            raise IndexError('size limit')

    def pop_back(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        pop_tail = self.items[self.tail]
        self.items[self.tail] = None
        self.tail = (self.tail - 1) % self.max_m
        self.size -= 1
        return pop_tail

    def pop_front(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        prev_head = (self.head + 1) % self.max_m
        item_prev_head = self.items[prev_head]
        self.items[prev_head] = None
        self.head = prev_head
        self.size -= 1
        return item_prev_head


def load_deque():
    n = int(input())
    m = int(input())
    deque = Deque(m)
    for i in range(n):
        c = input().split()
        try:
            if c[0] == 'pop_back':
                print(deque.pop_back())
            elif c[0] == 'pop_front':
                print(deque.pop_front())
            elif c[0] == 'push_back':
                deque.push_back(c[-1])
            else:
                deque.push_front(c[-1])
        except IndexError:
            print('error')


if __name__ == '__main__':
    load_deque()
