'''
ЗАМЕТКИ
------------------
AttributeError - сделать exception



'''

#model.py

import numpy as np
import re
import codecs
       
class Node ():
    def __init__ (self, stell_name, _full_file_str):
        self.first_name = stell_name
        self.mark = 0
        self.names, self.neighbours = \
            self._read_neighbours(_full_file_str, self.first_name, )
    
    def _read_neighbours(self, full_file_str, name):
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
        
        names = np.array([name], dtype = '<U13')
        neighbours = np.array(neighbours, dtype = '<U13')
        
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
        return (names, neighbours)

    def _get_regex(self, template:str):
        return re.compile(template)
        
    def _find_str (self, regex, object_str):
        _match = regex.search(object_str)
        return _match.group()

class Graph ():
    def __init__(self, file_name:str):
        self.file_name = file_name
        self.constellations = self._read_constellations(file_name)

    def _read_constellations (self, file_name):
        with codecs.open(file_name, encoding='utf-8') as file:
            full_file_str = file.read()
            file.close()
        stell_dict = {full_file_str[:3] : Node(full_file_str[:3], full_file_str)}
        stell_regex = self._get_regex('\\n\w\w\w')
        stell_str_list = stell_regex.findall(full_file_str)
        for i in range(len(stell_str_list)):
            stell_str_list[i] = stell_str_list[i][1:]
            stell_dict.update({stell_str_list[i] : Node(stell_str_list[i],
                               full_file_str)})
        return stell_dict
        
        
    def _get_regex(self, template:str):
        return re.compile(template)
        
    def _find_str (self, regex, object_str):
        _match = regex.search(object_str)
        return _match.group()

if __name__ == "__main__":
    print("This module is not for direct call!")

'''           
G = Graph('Data.txt')
print(G.constellations['Crv'].names)
'''     
        
        
        