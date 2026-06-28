aaa = input('PA ou PG? ').lower()
numero = int(input('Escolha o primeiro número: '))
termo = int(input('Qual posição você quer? '))
razao = int(input('Qual é a razão? '))
contador = 0
if aaa == "pa":
    while contador < termo + 1:
        resultado_pa = numero + (contador - 1) * razao
        print(resultado_pa)
        contador += 1

elif aaa == "pg":
    while contador < termo + 1:
        resultado_pg = numero * razao ** (contador - 1)
        print(resultado_pg)
        contador += 1

else:
    print("Opção inválida. Escolha PA ou PG.")
