from shape import Şekil

class Çember(Şekil):
    def __init__(self, yarıçap):
        super().__init__()
        self._yarıçap = yarıçap

    def alan_hesapla(self):
        self._alan = 3.14 * self._yarıçap ** 2

    def çevre_hesapla(self):
        self._çevre = 2 * 3.14 * self._yarıçap

    def __str__(self):
        return super().__str__() + f", Yarıçap: {self._yarıçap}"
