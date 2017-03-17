# -*- coding: utf-8 -*-
from controllers.merge_sort import MergeSort
class Main:

    # Cambiar los valores desordenados para genear una lista ordenada !!!!!!!
    list_scrambled = [4, 5, 2, 1, 6, 7, 8, 3]
    list_organized = []

    def __go_merge(self):
        # Creamos el objeto y corremos su metodo de mezcla
        merge_toy = MergeSort(self.list_scrambled)
        self.list_organized = merge_toy.run_merge()

    def __list_print(self):
        print('\n\nLista desordenada ...')
        print(self.old_list)
        print('\n Lista ordenada ...')
        print(self.list_organized)

    def __init__(self):
        # LLenando una lista desordenada
        size = len(self.list_scrambled)
        self.old_list = []
        for i in range(size):
            self.old_list.append(self.list_scrambled[i])
        self.__go_merge()
        self.__list_print()

if __name__ == '__main__':
    my_merge = Main()
