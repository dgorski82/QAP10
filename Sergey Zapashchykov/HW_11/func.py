from abc import ABC, abstractmethod


class Methods(ABC):

    @abstractmethod
    def addition(self, num_1, num_2):
        pass

    @abstractmethod
    def subtraction(self, num_1, num_2):
        pass

    @abstractmethod
    def multiplication(self, num_1, num_2):
        pass

    @abstractmethod
    def division(self, num_1, num_2):
        pass
