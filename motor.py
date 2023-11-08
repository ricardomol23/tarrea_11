class Motores:
    def __init__(self, cambio=1, rpm=500, consumo=0.05 ):
        self.cambio = cambio  
        self.rpm = rpm 
        self.consumo = consumo

    def arrancar(self):
        self.cambio = 1
        self.rpm = 500

    def subirCambio(self):
        if self.cambio < 5:
            self.cambio += 1

    def bajarCambio(self):
        if self.cambio > 1:
            self.cambio -= 1

    def subirRPM(self, cuantos):
        self.rpm += cuantos
        if self.rpm > 5000:
            self.rpm = 5000

    def bajarRPM(self, cuantos):
        self.rpm -= cuantos
        if self.rpm < 500:
            self.rpm = 500

    def velocidad(self):
        velocidad = (self.rpm / 100) * (0.5 + (self.cambio / 2))
        return velocidad

    def consumoActualPorKm(self):
        consumo = self.consumo
        if self.rpm > 3000:
            consumo *= (self.rpm - 2500) / 500
        if self.cambio == 1:
            consumo *= 3
        elif self.cambio == 2:
            consumo *= 2
        return consumo

# Ejemplo de uso:
#motor = Motores()
#motor.arrancar()
#motor.subirCambio()
#motor.subirRPM(3500)
#velocidad_actual = motor.velocidad()
#consumo = motor.consumoActualPorKm()
#print("Velocidad actual:", velocidad_actual)
#print("Consumo actual por km:", consumo)
# Ejemplo de uso:
motor_1 = Motores(cambio=1, rpm=5000, consumo=0.05)

# Calculamos el consumo
consumo = motor_1.consumoActualPorKm()
print("Consumo actual por km:", consumo)