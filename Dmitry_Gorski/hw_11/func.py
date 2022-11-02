from abc import ABC, abstractmethod


Operation = {'%': '__mod__', '*': '__mul__', '**': '__pow__', '+': '__add__',
             '-': '__sub__', '/': '__truediv__', '//': '__floordiv__'}


class Methods(ABC):

    @abstractmethod
    def calculate(self, *args, **kwargs):
        pass
