"""
Посылка 62032444

Спринт 4. Задача B. Хеш-таблица

По условию задачи необходимо реализовать собственную "Хэш-таблицу" на языке Python без использования
встроенной в язык реализации хэш-таблицы.
Необходимо реализовать несколько методов у данной хэш-таблицы:
- put key value —– добавление пары ключ-значение. Если заданный ключ уже есть в таблице, то соответствующее
ему значение обновляется.
- get key –— получение значения по ключу. Если ключа нет в таблице, то вывести «None». Иначе вывести
найденное значение.
- delete key –— удаление ключа из таблицы. Если такого ключа нет, то вывести «None», иначе вывести
хранимое по данному ключу значение и удалить ключ.


--ПРИНЦИП РАБОТЫ--

Хэш-таблица реализована на основе массива размером 10^5.
Разрешение коллизий реализуется с помощью метода цепочек. То есть с помощью связного списка.

Для этого создан класс Node для создания элементов связного списка.

Сама хэш-таблица реализована на основе класса Hash.

Обработка запросов производится по мере их поступления.

Метод get() реализован следующим образом. На вход поступает ключ для поиска по массиву.
С помощью хэш-функции hash_func() вычисляем значение индекса массива.
Если по данному индексу в таблице ничего нет (значение None), то функция сразу возвращает None.
Иначе получаем голову связного списка по индексу.
Далее вызываем метод search() для поиска элемента связного списка по индексу.
Реализован метод search на том, что проходим по всему связному списку и ищем по ключу данный
конкретный элемент списка, а так для метода delete() находим предыдущий элемент для искомого элемента,
то есть previous_node.
Если находим этот элемент, то метод get возвращает значение данного элемента.
Если не находим, то search, а за ней get возвращает значение None.

Метод put() реализован следующим образом. На вход поступает два аргумента: ключ и значение. Их необходимо
либо записать в хэш-таблицу, либо обновить значение.
Находим индекс массива через хэш-функцию. Создаем элемент связного списка node. Далее проверяем по
индексу наличие другого элемента в массиве. Если в этой ячейке массива ничего не записано, то записываем
ранее созданный элемент связного списка в эту ячейку массива.
Иначе получаем голову связного списка и вызываем функцию search. Передаем в нее голову и ключ для поиска.
Если не находим в связном списке элемента с таким ключом, то записываем его в качестве головы в связный
список. Иначе для найденного элемента меняем значение на новое.

Метод delete() реализован следующим образом. На вход получаем ключ для поиска. С помощью хэш-функции
проверяем наличие элемента в массиве. Если в нем ничего нет, тогда возвращаем None. Иначе получаем
голову списка и передаем ее с ключом для поиска в search. Если ничего не найдено, возвращаем None.
Иначе нам необходимо найти предыдущий элемент связного списка previous_node, через метод search().
Так же находим следующий элемент списка после иского элемента
таким образом next_node = search_node.next_item.
Если previous_node нет, тогда мы ячейку массива обозначаем, как None, и возвращаем значение
удаленного элемента.
Иначе если previous_node есть, тогда перезаписываем связь предыдущего элемента связного списка на
следующий элемент после искогомо, то есть previous_node.next_item = next_node.next_item.
После этого возвращаем значение удаленного элемента.


--ВРЕМЕННАЯ СЛОЖНОСТЬ--

В среднем все операции выполняются за O(1).


--ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ--

Значение пространственной сложности составит O(max(n, m), где n - количество добавленных ключей,
а m - количество корзин.
"""


class Node:
    def __init__(self, key, value, next_item=None):
        self.key = key
        self.value = value
        self.next_item = next_item


class Hash:
    def __init__(self):
        self.size = 10 ** 5
        self.tab = [None] * self.size

    def hash_func(self, key):
        return key % self.size

    def search(self, node, item):
        previous_node = None
        head = node
        while head:
            if head.key == item:
                return head, previous_node
            previous_node = head
            head = head.next_item
        return None, None

    def get(self, key):
        hash = self.hash_func(key)
        if self.tab[hash] is None:
            return None
        node = self.tab[hash]
        get_result, _ = self.search(node, key)
        if get_result is None:
            return None
        return get_result.value

    def put(self, key, value):
        node = Node(key, value)
        hash = self.hash_func(key)
        if self.tab[hash] is None:
            self.tab[hash] = node
        else:
            head = self.tab[hash]
            search_node, _ = self.search(head, key)
            if search_node is None:
                node.next_item = head
                self.tab[hash] = node
            else:
                search_node.value = node.value

    def delete(self, key):
        hash = self.hash_func(key)
        head = self.tab[hash]
        if head is None:
            return None
        search_node, previous_node = self.search(head, key)
        if search_node is None:
            return None
        next_node = search_node.next_item
        if previous_node is None:
            self.tab[hash] = search_node.next_item
        else:
            previous_node.next_item = next_node.next_item
        return search_node.value


if __name__ == '__main__':
    obj = Hash()
    n = int(input())
    for _ in range(n):
        s = [i for i in input().split()]
        if s[0] == 'get':
            print(obj.get(int(s[1])))
        elif s[0] == 'put':
            obj.put(int(s[1]), int(s[2]))
        else:
            print(obj.delete(int(s[1])))
