"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC, abstractmethod

class IJanela(ABC):

    @abstractmethod
    def fechar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IJanela):

    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanela):
    
    def maximizar(self):
        pass

    def minimizar(self):
        pass

    def fechar(self):
        pass


