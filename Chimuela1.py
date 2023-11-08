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

# Ejemplo de uso:
Chimuela = Chimuela()
Chimuela.comer(100)
Chimuela.volar(10)
Chimuela.volar(20)
print(Chimuela.energia())
