"""
Посылка 63739231

Спринт 5. Задача B. Удали узел

По условию задачи необходимо в бинарном дереве поиска, в котором хранятся ключи, найти ключ
и произвести его удаление так, чтобы дерево осталось корректным бинарным деревом поиска.
Если ключа в дереве нет, то изменять дерево не надо.
На вход вашей функции подаётся корень дерева и ключ, который надо удалить.


--ПРИНЦИП РАБОТЫ--

В рамках реализации алгоритма удаления узла бинарного дерева по заданному ключу использутся
функция remove(). На вход данной функции передается корень дерева и ключ, по которому необходимо
найти нужный для удаления узел.
Для начала необходимо произвести поиск удаляемого узла, поэтому проходим по левым или правым потомкам
вершин дерева, в случае если ключ меньше или же больше значения вершины.
После того, как ключ найден, приступаем к удалению данного узла. Для этого проверяем, есть ли у
удаляемого узла потомки. В самом просто случае, когда потомков нет, происходит удаление узла.
В случае, если потомки есть, необходимо с помощью вспомогательной функции search_min() найти минимальный
элемент дерева, для этого проходим по всем левым элементам поддерева, используя функцию поиска минимального
элемента search_min() и находим этот элемент.
Далее удаляемая вершина дерева заменяется на минимальный элемент дерева, который был найден с помощью
функции search_min(). Дальше происходит удаление этого минимального узла дерева с помощью рекурсивного
вызова функции remove().


--ВРЕМЕННАЯ СЛОЖНОСТЬ--

Временная сложность удаления искомого узла составляет O(h), где h - высота дерева.
Сама временная сложность зависит от высоты дерева h. В случае сбалансированного двоичного
дерева алгоритм удаления будет точно зависеть именно от высоты дерева h - это можно назвать
лучшим вариантом для решения задачи (если так можно выразиться, то идеальным). Так же можно
считать, что в среднем алгоритм работает за O(logN).
В другом же случае - несбалансированности дерева, эффективность использования двоичного дерева
становится нецелесообразным. Временная сложность практически линейно зависит от размера самого
дерева, то есть O(n). Задачу в таком случае целесообразно решать с помощью связных списков.


--ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ--

В случе с бинарным деревом поиска при использовании рекурсивных вызовов функции remove(), можно
считать, что пространственная сложность алгоритма удаления узла дерева зависит от высоты дерева h
и составляет O(h). В худшем случае, когда дерево не сбалансированное, можно считать, что
пространственная сложность составляет O(n), то есть линейно зависит от входных данных (или размера
самого дерева). В данном случае при рекурсивных вызовах функции remove() и при больших размерах
дерева это может привести к переполнению стека вызовов.
"""


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def search_min(root):
    while root.left:
        root = root.left
    return root


def remove(root, key):
    if root is None:
        return None
    if key < root.value:
        root.left = remove(root.left, key)
        return root
    if key > root.value:
        root.right = remove(root.right, key)
        return root

    if root.left is None:
        return root.right
    if root.right is None:
        return root.left
    min_key = search_min(root.right)
    root.value = min_key.value
    root.right = remove(root.right, min_key.value)
    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8
