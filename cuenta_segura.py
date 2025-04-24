class CuentaSegura:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial #metodo privado real
        self._historial = []  #metodo protegido

    @property
    def saldo(self): #"""Propiedad de solo lectura para consultar el saldo"""
        return self.__saldo

    @saldo.setter
    def saldo(self, valor): #"""setter para asignas saldo solo si es un numero no negativo"""
        if not isinstance(valor, (int, float)):
                raise ValueError("El saldo debe ser un numero.")
            
        if valor < 0:
                raise ValueError("El saldo no puede ser negativo")
        self.__saldo = valor

    def depositar(self, cantidad):
        if cantidad <= 0:
                raise ValueError("La cantidad a depositar debe ser mayor a cero")
        self.__saldo += cantidad
        self._historial.append(f"+{cantidad}")

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero")

        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= cantidad
        self._historial.append(f"-${cantidad}")

    def mostrar_historial(self): #metodo publico que abstrae el detalle de como se guarda el historial
        print("Historial de transacciones:" ", ".join(self._historial))

cuenta = CuentaSegura("Maria", 100)
print("Titular", cuenta.titular)
print("Saldo inicial: ", cuenta.saldo)

cuenta.depositar(50)
cuenta.retirar(30)
print("Saldo actual: ", cuenta.saldo)


try:
    cuenta.saldo = -10
except ValueError as e:
    print("Error al asignar saldo ", e)

cuenta.mostrar_historial