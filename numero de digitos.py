'''
7. Escreva a função que recebe como parâmetro um número inteiro longo e retorna quantos dígitos
o número possui. Não converta o número para string, lista ou tupla. Exemplo: 1987545 possui 7
dígitos.

'''
def numerodedig(n): #Definindo a funcao do numero de digitos
    d=0 #Iniciando a variavel da quantidade de digitos
    while n!=0: #Quando o número for igual termina o ciclo...
        n=n//10 #Basta ir dividindo o número por 10 e fazendo o arredondamento a unidades com esse contador ocorre o incremento
        d=d+1   #Aumentar o contator sempre que passar um ciclo
    return d #Retorna a quantidade dígitos para a funcao
print(numerodedig(9999)) #Mostra a quantidade de dígitos do número 9999