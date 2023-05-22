from shape import Şekil

class Dikdörtgen(Şekil):
    def __init__(self, uzunluk, genişlik):
        super().__init__()
        self._uzunluk = uzunluk
        self._genişlik = genişlik

    def alan_hesapla(self):
        self._alan = self._uzunluk * self._genişlik

    def çevre_hesapla(self):
        self._çevre = 2 * (self._uzunluk + self._genişlik)

    def çiz(self):
        for i in range(self._genişlik):
            print('*' * self._uzunluk)

    def __str__(self):
        return super().__str__() + f", Uzunluk: {self._uzunluk}, Genişlik: {self._genişlik}"
