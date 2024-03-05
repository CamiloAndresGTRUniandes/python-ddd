from abc import ABC, abstractmethod

class View(ABC):

    @abstractmethod
    def get_by(**kwargs):
        ...