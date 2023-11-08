class Enterprise:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5

    def encontrarPilaAtomica(self):
        self.potencia = min(self.potencia + 25, 100)

    def encontrarEscudo(self):
        self.coraza = min(self.coraza + 10, 20)

    def recibirAtaque(self, puntos):
        d_coraza = min(self.coraza, puntos)
        d_potencia = max(puntos - self.coraza, 0)
        self.coraza -= d_coraza
        self.potencia = max(self.potencia - d_potencia, 0)

    def fortalezaDefensiva(self):
        return self.coraza + self.potencia

    def necesitaFortalecerse(self):
        return self.coraza == 0 and self.potencia < 20

    def fortalezaOfensiva(self):
        return max(0, (self.potencia - 20) // 2)

    def obtener_potencia(self):
        return self.potencia

    def obtener_coraza(self):
        return self.coraza
enterprise = Enterprise()
print("Potencia inicial:", enterprise.obtener_potencia())
print("Coraza inicial:", enterprise.obtener_coraza())
print("Fortaleza Defensiva:", enterprise.fortalezaDefensiva())
print("Necesita Fortalecerse:", enterprise.necesitaFortalecerse())
print("Fortaleza Ofensiva:", enterprise.fortalezaOfensiva())