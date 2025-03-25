class TarjetaCredito:
    def _init_(self, numero):
        self.numero = numero

    @staticmethod
    def validar_tarjeta(numero):
        digitos = list(map(int, str(numero)))
        suma_total = 0

        for i, digito in enumerate(reversed(digitos)):
            if i % 2 == 1:
                digito *= 2
                if digito > 9:
                    digito -= 9
            suma_total += digito

        return suma_total % 10 == 0

    def es_valida(self):
        return self.validar_tarjeta(self.numero)

tarjeta = TarjetaCredito(4532015112830366)
print(f"El número de tarjeta {tarjeta.numero} es {'válido' if tarjeta.es_valida() else 'inválido'}.")