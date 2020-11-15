import abc
from abc import ABCMeta

class StructureData(object):
    __metaclass__ = ABCMeta

    @abc.abstractclassmethod
    def print(self):
        print('Método abstracto para imprimir')