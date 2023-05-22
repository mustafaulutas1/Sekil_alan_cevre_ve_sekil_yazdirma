from shape import Şekil

class Üçgen(Şekil):
    def __init__(self, kenar1, kenar2, kenar3):
        super().__init__()
        self._kenar1 = kenar1
        self._kenar2 = kenar2
        self._kenar3 = kenar3

    def alan_hesapla(self):
        s = (self._kenar1 + self._kenar2 + self._kenar3) / 2
        self._alan = (s * (s - self._kenar1) * (s - self._kenar2) * (s - self._kenar3)) ** 0.5

    def çevre_hesapla(self):
        self._çevre = self._kenar1 + self._kenar2 + self._kenar3

    def çiz(self):
        for i in range(self._kenar1):
            print('*' * (i + 1))

    def __str__(self):
        return super().__str__() + f", Kenar 1: {self._kenar1}, Kenar 2: {self._kenar2}, Kenar 3: {self._kenar3}"
