escolha = input('PA ou PG? '\n).lower()
numero = int(input('Escolha o primeiro número: '\n))
termo = int(input('Qual posição você quer? '\n))
razao = int(input('Qual é a razão? '\n))
contador = 0
if escolha == "pa":
    while contador < termo + 1:
        resultado_pa = numero + (contador - 1) * razao
        print(resultado_pa)
        contador += 1

elif escolha == "pg":
    while contador < termo + 1:
        resultado_pg = numero * razao ** (contador - 1)
        print(resultado_pg)
        contador += 1

else:
    print("Opção inválida. Escolha PA ou PG.")
