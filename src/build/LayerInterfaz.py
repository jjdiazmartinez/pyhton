from abc import abstractmethod
from abc import ABCMeta
class  LayerInterfaz(metaclass=ABCMeta):
    @abstractmethod
    def buildComponent(self, structure):
        pass


