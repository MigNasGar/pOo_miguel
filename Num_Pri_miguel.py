num = int(input("Digite um número positivo: ")) #resposta do user é definida como uma variável
contador = 0

for i in range(1, num + 1): #define o range de i, que vai de 1 até num+1 até chegar no valor de num
    if num % i == 0:
        contador += 1 #testa os divisores somando 1 ao valor anterior

print("O número {} foi divisível {} vezes!".format(num, contador))

if contador == 2: #se o total de vezes que o num foi dividido for 2 o número sera primo
    print("O número é primo")
else: #se o total for 2 divisões ou mais o número não sera primo
    print("O número não é primo")
