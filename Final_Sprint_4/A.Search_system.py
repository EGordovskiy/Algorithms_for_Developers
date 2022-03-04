"""
Посылка 61956058

Спринт 4. Задача A. Поисковая система

По условию задачи необходимо реализовать "Поисковую систему", которая будет определять релевантность
запросов относительно документов. То есть на вход приходит некоторое количество документов и запросов,
алгоритм определяет насколько релевантны документы для запросов и выводит 5 наиболее релевантных запросам
документов по убыванию (от большего к меньшему).


--ПРИНЦИП РАБОТЫ--

На вход поступают данные о документах: количество документов и сам документ(-ы) одной строкой.
Вторая часть данных: количество запросов и сам запрос(-ы) одной строкой.
В результате работы функции обработки входных данных read_input() на выходе получаем два объекта
данных: table, queries.
table - словарь словарей, то есть мы получаем количество повторений конкретного слова в каждом документе.
table, например, для документа i love coffee, имеет вид:
{'i': {1: 1}, 'love': {1: 1}, 'coffee': {1: 1, 2: 1}}.
querys - это массив множеств, то есть в результате обработки запросов, получаем множество уникальных
элементов (слов) запроса. Например, [{'milk', 'black', 'i', 'without', 'like', 'coffee'}].

Данные полученные в результате работы read_input() передаются в функцию check() в качестве аргументов.
Далее в check() идет первая пара вложенных циклов для поиска каждого конкретного слова запроса в таблице
table по ключу, то есть количество повторений слова-ключа в табилце table. Результат сохраняем в
промежуточном массиве check_result = [].

Далее уже по каждому элементу check_result проходим и определяем уже количество повторений для
каждого конкретного слова в конкретном документе, то есть релевантность. Результат сохраняется в
tab_result = {}, далее каждый конкретный набор данных для одного запроса сортируется и выводится
на печать для 5-ти наиболее релевантных документов.


--ВРЕМЕННАЯ СЛОЖНОСТЬ--

Временная сложность при реализации функции обработки входных данных read_input() будет складываться из
нескольких составляющих.
При первой обработке документов и составлении хэш-таблицы временная сложность будет O(n*w1), то есть
мы обрабатываем n-количество документов с w1 слов в каждом.
При обработке запросов временная сложность будет аналогична первому случаю, но зависит уже от количества
запросов m и количества документов в каждом запросе w2, то есть О(m*w2).
В общем временная сложность при обработке входных данных будет O(n*w1 + m*w2).

При реализации второй функции check() так же временная сложность составляет O(w2*d + dlogd),

### комментарий ревьюера
Текущая оценка говорит что для каждого слова нужно сортировать поисковую выдачу, но сортировать
нужно 1 раз для всего запроса. Правильно будет: O(m*(w2*d + dlogd))
###

то есть
для каждого слова запроса получаем поисковую выдачу, которую необходимо отсортировать.
При этом данную операцию необходимо проводить для каждой единицы запроса m. Таким образом общая
временная сложность составит O(m(w2*d + dlogd)).


--ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ--

Общая пространственная сложность при реализации первой функции обработки входных данных будет состоять
из общего размера хэш-таблицы размером n-количество документов с количеством слов в каждом документе w1.
C вложенными словарями по количеству докуметов n. То есть для реализации таблицы будет задействовано
O(n*w1 + n) памяти.
При обработке данных по запросам получаем список списков размером m-количество запросов.
Что в общем случае для первой функции дает O(n*w1 + n + m).

В рамках реализации второй функции check() используется дополнительная память на хранение
результатов поисковой выдачи d и каждого уникального слова запроса. Таким обрзаом
дополнительная память составляем O(w2+d).

### комментарий ревьюера
результатов поисковой выдачи d и каждого уникального слова запроса значит O(w2 + d).
Умножение значит, что для каждого слова нужно хранить поисковую выдачу отдельно.
O(w2*d) будет правильно в худшем случае, если d - среднее количество документов в
индексе для конкретного слова.
###

Далее используется дополнительная память для хранения результатов обработки найденных раннее
данных и зависит от количества запросов m, от данных из хэш-табилицы для каждого слова n*w1.
Далее используется дополнительная память на хранение результата обработки каждого элемента
поисковой выдачи, то есть d1. Таким образом на данном этапе дополнительная память займет O(d1),
так как мы обрабатываем каждый конкретный элемент поисковой выдачи и после этого выводим результаты
на печать.
То есть общая пространственная сложность составит O(w2+d + d1).
"""


def read_input():
    n = int(input())
    table = {}
    for doc_num in range(1, n + 1):
        doc = input().split()
        for word in doc:
            if word not in table:
                table[word] = dict({doc_num: 1})
            else:
                table[word][doc_num] = table[word].get(doc_num, 0) + 1

    m = int(input())
    queries = [input().split() for _ in range(1, m + 1)]
    return table, queries


def check(table, queries):
    check_result = []
    for query in queries:
        tab_middle = []
        for word in set(query):
            if word in table.keys():
                tab_middle.append(table[word])
        check_result.append(tab_middle)

    for docs in check_result:
        tab_result = {}
        for doc in docs:
            for key, val in doc.items():
                if key not in tab_result.keys():
                    tab_result[key] = val
                else:
                    tab_result[key] += val
        c = sorted(tab_result.keys(), key=lambda x: (-tab_result[x], x))
        print(' '.join(map(str, c[:5])))


if __name__ == '__main__':
    table, queries = read_input()
    search_results = check(table, queries)