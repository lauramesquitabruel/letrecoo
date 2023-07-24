import random
from valid_words import valid

palavra_gerada = random.choice(valid)
chances = 7

class Cores:
    PREFIX = '\033'
    BASE = "\033[0m"
    GREY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"

class PalavraCerta:
    contador = 1
    def __init__(self, palavra_str:str):
        self.palavra_str = palavra_str
        self.palavra_chars = list(self.palavra_str)
        self.palavra_tentada_str = ""
    
    def conta_chances(self):
        PalavraCerta.contador += 1

    def valida_tentavivas(self):
       return self.palavra_str in valid 
    
    def deixa_verdinho(self):
        for i, char in enumerate(self.palavra_chars):
            letra = palavra_gerada[i]
            letra_tentada = self.palavra[i]
            if letra == letra_tentada:
                letra_colorida = f"{Cores.GREEN}{letra}{Cores.BASE}"
                self.palavra_chars[i] = letra_colorida

    def tentativas(self):
        self.deixa_verdinho()
        self.palavra_tentada_str = "".join(self.palavra_chars)
        print(self.palavra_tentada_str)
