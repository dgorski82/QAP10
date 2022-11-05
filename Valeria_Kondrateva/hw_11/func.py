from abc import ABC, abstractmethod


class Methods(ABC):

    @abstractmethod
    def addition(self, num1, num2):
        pass

    @abstractmethod
    def subtraction(self, num1, num2):
        pass

    @abstractmethod
    def multiplication(self, num1, num2):
        pass

    @abstractmethod
    def division(self, num1, num2):
        pass
