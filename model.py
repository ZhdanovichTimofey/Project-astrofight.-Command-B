'''
ЗАМЕТКИ
------------------
AttributeError - сделать exception
is_neighbours - реализовать через exception в мейне, так сильно быстрее

branch test
'''

# model.py

import numpy as np
import re
import codecs
       

class Node:
    '''
    Класс, реализующий вершину двуцветного графа созвездий и ставящий 
    каждому созвездию в соответсвие его имена на русском и латинском а также
    его соседей.
    ---------------------------------------------------------------------------
    stell_name - трёхбуквенное имя созвездия, которому соответствует 
    эта вершина;
    _full_file_str - внутренняя переменная, получаемая при вызове из
    класса Graph, которая содержит информацию о звездном небе в виде строки.
    '''
    def __init__(self, stell_name, _full_file_str):
        self.first_name = stell_name
        self.mark = 0
        self.names, self.neighbours = \
            self._read_neighbours(_full_file_str, self.first_name, )
    
    def _read_neighbours(self, full_file_str, name):
        '''
        Приватный метод, находящий для данного созвездия всех его соседей и
        все его имена с помощью поиска в строке full_file_str. Вызывается
        при инициализации.
        -----------------------------------------------------------------------
        name - трёхбуквенное имя созвездия, для которого производится поиск;
        full_file_str - переменная, которая содержит информацию о
        звездном небе в виде строки.
        '''
        find_regex = self._get_regex(name + '(-\w+)+:(-\w+)+\.')
        namesList_regex = self._get_regex(name + '(-\w+)+' + '\:')
        neighboursList_regex = self._get_regex('\:' + '(-\w+)+' + '\.')
        
        find_str = self._find_str(find_regex, full_file_str)
        del full_file_str
        namesList_str = self._find_str(namesList_regex, find_str)
        neighboursList_str = self._find_str(neighboursList_regex, find_str)
        
        neighbour_regex = self._get_regex('-\w+')
        namePart_regex = self._get_regex('-\w+')
        
        neighbours = neighbour_regex.findall(neighboursList_str)
        for i in range(len(neighbours)):
            neighbours[i] = neighbours[i][1:]
        
        nameParts = namePart_regex.findall(namesList_str)
        for i in range(len(nameParts)):
            nameParts[i] = nameParts[i][1:]
        
        names = np.array([name], dtype='<U13')
        neighbours = np.array(neighbours, dtype='<U13')
        
        if len(nameParts) == 2:
            names = np.append(names, nameParts)
        elif len(nameParts) == 3:
            part_LAT = nameParts[0]
            part_RU = nameParts[1] + ' ' + nameParts[2]
            nameParts = [part_LAT, part_RU]
            names = np.append(names, nameParts)
        elif len(nameParts) == 4:
            part_LAT = nameParts[0] + ' ' + nameParts[1]
            part_RU = nameParts[2] + ' ' + nameParts[3]
            nameParts = [part_LAT, part_RU]
            names = np.append(names, nameParts)
        return names, neighbours

    def _get_regex(self, template: str):
        '''
        Приватный метод, возвращает регулярное выражение по строке.
        -----------------------------------------------------------------------
        template - строка-шаблон для создания регулярного выражения.
        '''
        return re.compile(template)
        
    def _find_str(self, regex, object_str):
        '''
        Приватный метод, возвращает один, первый, результат поиска в строке
        по регулярному выражению.
        -----------------------------------------------------------------------
        regex - регулярное выражение, по которому происходит поиск;
        object_str - строка, в которой происходит поиск.
        '''
        _match = regex.search(object_str)
        return _match.group()
    

class Graph:
    '''
    Класс, реализующий двуцветный граф созвездий в виде словаря "трехбуквенное
    обозначение созвездия : объект Node этого созвездия".
    ---------------------------------------------------------------------------
    file_name - имя файла, в котором содержится информация о звёздном небе.
    '''
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.constellations = self._read_constellations(file_name)

    def _read_constellations(self, file_name):
        '''
        Приватный метод, читающий файл и возвращающий словарь созвездий.
        Вызывается при инициализации.
        -----------------------------------------------------------------------
        file_name - имя файла, откуда производится чтение.
        '''
        with codecs.open(file_name, encoding='utf-8') as file:
            full_file_str = file.read()
            file.close()
        stell_dict = {full_file_str[:3]: Node(full_file_str[:3], full_file_str)}
        stell_regex = self._get_regex('\\n\w\w\w')
        stell_str_list = stell_regex.findall(full_file_str)
        for i in range(len(stell_str_list)):
            stell_str_list[i] = stell_str_list[i][1:]
            stell_dict.update({stell_str_list[i]: Node(stell_str_list[i],
                               full_file_str)})
        return stell_dict

    def _get_regex(self, template: str):
        '''
        Приватный метод, возвращает регулярное выражение по строке.
        -----------------------------------------------------------------------
        template - строка-шаблон для создания регулярного выражения.
        '''
        return re.compile(template)

    def is_neighbours (self, stell:Node, step_name:str):
        '''
        Публичный метод, позволяющий определить, граничит ли указанное
        созвездие с текущим, возвращает объект Node, отвечающий за проверяемое
        созвездие, если они граничат и 0, если нет.
        -----------------------------------------------------------------------
        stell - объект Node, соответствующий текущему созвездию; 
        step_name - имя созвездия для проверки.
        '''
        for i in stell.neighbours:
            if step_name in self.constellations[i].names:
                return self.constellations[i]
        return False
