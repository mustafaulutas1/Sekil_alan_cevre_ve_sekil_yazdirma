from rectangle import Dikdörtgen
from triangle import Üçgen
from circle import Çember

# Dikdörtgen örneği
print("Dikdörtgen:")
dikdörtgen = Dikdörtgen(8, 8)
dikdörtgen.alan_hesapla()
dikdörtgen.çevre_hesapla()
print(dikdörtgen)
dikdörtgen.çiz()
print("\n")
# Üçgen örneği
print("Üçgen:")
üçgen = Üçgen(5, 5, 5)
üçgen.alan_hesapla()
üçgen.çevre_hesapla()
print(üçgen)
üçgen.çiz()
print("\n")
# Çember örneği
print("Çember:")
çember = Çember(7)
çember.alan_hesapla()
çember.çevre_hesapla()
print(çember)
 