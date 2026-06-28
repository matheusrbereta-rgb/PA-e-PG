aaa = str(input('PA ou PG: \n')).lower().strip()
numero = float(input('Escolha um numero a ser multiplicado: \n'))
termo = float(input('O valor que multiplica o numero: \n'))
if aaa == "pa":
    termo_todo = input('todos termos ou somente o ultimo?')
    print("Primeiros 5 termos da PA:")
    for i in range(1, 6):
        print(numero + (i-1) * termo)
    if termo_todo == "todos os termos" or 'tot' or 't':
        result =  termo * numero
        print(result)
    else:
        result = termo * numero 
        print(result)                   
elif aaa == 'pg':   
    termo_todo = input('todos termos ou somente ultimo?')
    print("Primeiros 5 termos da PG:")
    for i in range(1, 6):
        print(numero * (termo ** (i-1)))    
    if termo_todo in ["todos os termos", "tot", "t"]:
        result = numero * (termo ** 4)      
        print(result)
    else:
        result = numero * (termo ** 4)
        print(result)