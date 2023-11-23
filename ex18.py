def milhas_para_km(milhas):
    km = milhas * 1.61
    return km

def km_para_milhas(km):
    milhas = km / 1.61
    return milhas

def main():
    print("Escolha a conversão:")
    print("1. Milhas para Quilômetros")
    print("2. Quilômetros para Milhas")
    escolha = int(input())

    if escolha == 1:
        milhas = float(input("Digite a quantidade de milhas: "))
        km = milhas_para_km(milhas)
        print(f"{milhas} milhas equivalem a {km:.2f} quilômetros.")
    elif escolha == 2:
        km = float(input("Digite a quantidade de quilômetros: "))
        milhas = km_para_milhas(km)
        print(f"{km} quilômetros equivalem a {milhas:.2f} milhas.")
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()
