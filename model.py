#model.py

import numpy as np
import re
import codecs
       
class Node ():
    def __init__ (self, file_name:str, stell_name):
        self._file_name = file_name
        self.first_name = stell_name
        self.mark = 0
        self.names, self.neighbours = \
            self._read_neighbours(self._file_name, self.first_name)
    
    def _read_neighbours(self, file_name, name):
        find_regex = self._get_regex(name + '(-\w+)+:(-\w+)+\.')
        name_regex = self._get_regex(name + '(-\w+)+' + '\:')
        neighbour_regex = self._get_regex('\:' + '(-\w+)+' + '\.')
            
        with codecs.open('Data.txt', encoding='utf-8') as file:
            full_file_str = file.read()
            file.close()
            
        find_str = self._find_str(find_regex, full_file_str)
        name_str = self._find_str(name_regex, find_str)
        neighbour_str = self._find_str(neighbour_regex, find_str)
        
        
        
        
    def _get_regex(self, template:str):
        return re.compile(template)
        
    def _find_str (self, regex, object_str):
        _match = regex.search(object_str)
        return _match.group()


class Graph ():
    def __init__(self, file_name:str):
        self.file_name = file_name