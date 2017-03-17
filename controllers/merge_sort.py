# -*- coding: utf-8 -*-


class MergeSort:

    a_list = []

    def _merge_work(self, alist):
        print("delimito ", alist)
        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self._merge_work(lefthalf)
            self._merge_work(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i + 1
                else:
                    alist[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                alist[k] = righthalf[j]
                j = j + 1
                k = k + 1
        print("Mezclando ", alist)
        return (alist)

    def run_merge(self):
        list_new = self._merge_work(self.a_list)
        return list_new

    def __init__(self, a_list):
        self.a_list = a_list
