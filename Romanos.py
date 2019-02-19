import sys

class Romanos:
    def __init__(self):
        self.unidades = {
            0: "",
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX"
        }
        self.decenas = {
            0: "",
            1: "X",
            2: "XX",
            3: "XXX",
            4: "XL",
            5: "L",
            6: "LX",
            7: "LXX",
            8: "LXXX",
            9: "XC"
        }
        self.centenas = {
            0: "",
            1: "C",
            2: "CC",
            3: "CCC",
            4: "CD",
            5: "D",
            6: "DC",
            7: "DCC",
            8: "DCCC",
            9: "CM"
        }
        self.millares = {
            0: "",
            1: "M",
            2: "MM",
            3: "MMM"
        }
        
    def descomponer_numero(self, numero):
        digitos_enteros = []
        is_numero = True
        try:
            numero = int(numero)
        except:
            is_numero = False
        
        if is_numero:
            if numero < 1 or numero > 3999:
                digitos_enteros = None
            else:
                lista_digitos = list(str(numero))
                for digito in lista_digitos:
                    try:
                        digitos_enteros.append(int(digito))
                    except ValueError:
                        digitos_enteros = None
        else:
            digitos_enteros = None

        return digitos_enteros

    def transformar_numero(self, lista_digitos):
        numero = ""
        if lista_digitos != None:
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
    resultado = romano.transformar_numero(romano.descomponer_numero(sys.argv[1]))
    if  resultado == None:
        print("No se pude convertir en romano")
    else:
        print(resultado)