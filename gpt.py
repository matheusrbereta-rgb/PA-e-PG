aaa = input('PA ou PG? ').lower()
bbb = input('mult, div, exp ou raiz? ').lower()

numero = int(input('Escolha o primeiro número: '))
termo = int(input('Qual posição você quer? '))
razao = int(input('Qual é a razão? '))

if aaa == "pa":
    resultado_pa = numero + (termo - 1) * razao
    print(resultado_pa)

elif aaa == "pg":
    resultado_pg = numero * razao ** (termo - 1)
    print(resultado_pg)

else:
    print("Opção inválida. Escolha PA ou PG.")