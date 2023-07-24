import stoperdida

if __name__ == "__main__":
    with open("cheat.txt", "w") as f:
        f.write(stoperdida.palavra_gerada)
                
    while True:
        guess = stoperdida.PalavraCerta(
            palavra_str = input(">")
        )
        if guess.valida_tentavivas():
            guess.tentativas()
            guess.conta_chances()
            print(stoperdida.PalavraCerta.contador)
