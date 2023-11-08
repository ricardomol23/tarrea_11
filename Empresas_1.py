class Enterprise:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5

    def encontrarPilaAtomica(self):
        self.potencia = min(self.potencia + 25, 100)

    def encontrarEscudo(self):
        self.coraza = min(self.coraza + 10, 20)

    def recibirAtaque(self, puntos):
        if self.coraza >= puntos:
            self.coraza -= puntos
        else:
            puntos_restantes = puntos - self.coraza
            self.coraza = 0
            self.potencia = max(self.potencia - puntos_restantes, 0)

    def obtener_potencia(self):
        return self.potencia

    def obtener_coraza(self):
        return self.coraza

enterprise = Enterprise()
print("Potencia inicial:", enterprise.obtener_potencia())
print("Coraza inicial:", enterprise.obtener_coraza())

enterprise.encontrarPilaAtomica()
print("Potencia después de encontrar pila atómica:", enterprise.obtener_potencia())

enterprise.recibirAtaque(14)
print("Potencia después de recibir ataque:", enterprise.obtener_potencia())
print("Coraza después de recibir ataque:", enterprise.obtener_coraza())

enterprise.encontrarEscudo()
print("Potencia después de encontrar escudo:", enterprise.obtener_potencia())
print("Coraza después de encontrar escudo:", enterprise.obtener_coraza())