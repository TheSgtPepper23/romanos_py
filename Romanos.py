import sys

class Romanos:
    def __init__(self):
        self.unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        self.decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        self.centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        self.millares = ["", "M", "MM", "MMM"]
        
    def descomponer_numero(self, numero):
        try:
            numero = int(numero)
        except:
            raise
        
        digitos_enteros = []
        if numero > 1 and numero < 3999:
            lista_digitos = list(str(numero))
            for digito in lista_digitos:
                try:
                    digitos_enteros.append(int(digito))
                except:
                    raise

        return digitos_enteros

    def transformar_numero(self, lista_digitos):
        numero = ""
        if lista_digitos:
            if len(lista_digitos) == 4:
                numero = self.millares[lista_digitos[0]] + self.centenas[lista_digitos[1]] + \
                         self.decenas[lista_digitos[2]] + self.unidades[lista_digitos[3]]
            if len(lista_digitos) == 3:
                numero = self.centenas[lista_digitos[0]] + self.decenas[lista_digitos[1]] + \
                         self.unidades[lista_digitos[2]]
            if len(lista_digitos) == 2:
                numero = self.decenas[lista_digitos[0]] + self.unidades[lista_digitos[1]]
            if len(lista_digitos) == 1:
                numero = self.unidades[lista_digitos[0]]
        else:
            numero = None

        return numero

if __name__ == "__main__":
    romano = Romanos()
    try:
        resultado = romano.transformar_numero(romano.descomponer_numero(sys.argv[1]))
        if resultado != None:
            print(resultado)
        else:
            print("No puedo convertir ese número")
    except (ValueError, TypeError):
        print("Eso no es un número")
