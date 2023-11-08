class Chimuela:
    def __init__(self):
        self.energy = 0  # Inicializamos la energía de Chimuela en 0 joules

    def comer(self, gramos):
        # Chimuela gana 4 joules por cada gramo de comida que come
        self.energy += 4 * gramos

    def volar(self, kilometros):
        # Chimuela gasta 1 joule por cada kilómetro volado
        # Además, hay un costo de 10 joules por el despegue y aterrizaje
        self.energy -= (kilometros + 10)

    def energia(self):
        return self.energy

    def estaDebil(self):
        return self.energy < 50

    def estaFeliz(self):
        return 500 <= self.energy <= 1000

    def cuantoQuiereVolar(self):
        base = self.energy // 5
        if 300 <= self.energy <= 400:
            base += 10
        if self.energy % 20 == 0:
            base += 15
        return base

# Ejemplo de uso:
Chimuela = Chimuela()
Chimuela.comer(100)
Chimuela.volar(10)
Chimuela.volar(20)
print(Chimuela.energia())  # Debería imprimir 350
print(Chimuela.estaDebil())  # Debería imprimir False
print(Chimuela.estaFeliz())  # Debería imprimir False
Chimuela.comer(85)
print(Chimuela.cuantoQuiereVolar())  # Debería imprimir 68
