'''
3. Um número é capicua quando ele não muda se lido da esquerda para a direita ou da direita para
a esquerda. Por exemplo, o ano 2002 é um ano capicua. Elabora uma função que verifique essa
característica. A função deve retornar um valor booleano. Teste a execução da função.
'''
def capicua(numero):
    n=list(str(numero)) # converte o número pra uma string e transforma em uma lista
    if n==n[::-1]: # compara se a lista é igual seu reverso
        return True # retorna o valor true caso seja igual
    else:
        return False # e retorna o valor falso caso seja diferente
print(capicua(2002)) #verifica se o numero 2002 é capicua