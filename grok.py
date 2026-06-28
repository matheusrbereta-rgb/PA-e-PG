print("✅ Código arrumado DO JEITO QUE VOCÊ QUER: só 5 termos + o que você pediu, sem imprimir tudo!")

aaa = input('PA ou PG? ').lower().strip()

a1 = float(input('Digite o primeiro termo (a1): '))
n = int(input('Digite qual termo você quer (n): '))
r = float(input('Digite a razão (r): '))

if aaa == "pa":
    print("\n📋 Primeiros 5 termos da PA:")
    for i in range(1, 6):
        termo_atual = a1 + (i-1) * r
        print(f"Termo {i}: {termo_atual}")
    
    termo_pedido = a1 + (n-1) * r
    print(f"\n✅ O {n}º termo que você pediu é: {termo_pedido}")

elif aaa == "pg":
    print("\n📋 Primeiros 5 termos da PG:")
    for i in range(1, 6):
        termo_atual = a1 * (r ** (i-1))
        print(f"Termo {i}: {termo_atual}")
    
    termo_pedido = a1 * (r ** (n-1))
    print(f"\n✅ O {n}º termo que você pediu é: {termo_pedido}")
    
else:
    print("❌ Opção inválida! Digite só PA ou PG.")