from abc import ABC, abstractmethod

class Şekil(ABC):
    def __init__(self):
        self._alan = 0.0
        self._çevre = 0.0

    def get_alan(self):
        return self._alan

    def get_çevre(self):
        return self._çevre

    @abstractmethod
    def alan_hesapla(self):
        pass

    @abstractmethod
    def çevre_hesapla(self):
        pass

    def çiz(self):
        pass

    def __str__(self):
        return f"Alan: {self._alan}, Çevre: {self._çevre}"
